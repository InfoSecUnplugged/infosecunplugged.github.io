#!/usr/bin/env python3
"""
Static site generator for InfoSecUnplugged podcast website.

This module builds a complete static website from Jinja2 templates and YAML configuration
files. It generates HTML pages for the main page, episode listings, individual episodes,
tag pages, and series pages. The build process reads episode metadata, renders templates,
and writes the final HTML output to the appropriate directory structure.

Configuration:
    - Templates located in templates/ directory (Jinja2 format)
    - Episode metadata in config/episodes.yaml
    - Site configuration in config/config.yaml
    - Platform information in config/platforms.yaml
    - Markdown transcripts in transcripts/ directory

Output structure:
    - episodes/: Individual episode pages and index
    - tags/: Tag-based episode collections
    - series/: Episode series grouped by category
    - index.html: Main landing page
"""

import os
import markdown
import shutil
import yaml
from jinja2 import Environment
from slugify import slugify

main_template_file = "templates/index.j2.html"
episode_index_template_file = "templates/episode-index.j2.html"
episode_template_file = "templates/episode.j2.html"
serie_template_file = "templates/serie.j2.html"
tag_template_file = "templates/tag.j2.html"
config_data_file = "config/config.yaml"
episodes_data_file = "config/episodes.yaml"
platforms_data_tile = "config/platforms.yaml"


# Clean up previous build artifacts
if os.path.exists("episodes"):
    shutil.rmtree("episodes")
if os.path.exists("tags"):
    shutil.rmtree("tags")
if os.path.exists("series"):
    shutil.rmtree("series")

# Load all template files
with open(main_template_file, "r", encoding="utf-8") as fh:
    main_template_html = fh.read()
with open(episode_index_template_file, "r", encoding="utf-8") as fh:
    episode_index_template_html = fh.read()
with open(episode_template_file, "r", encoding="utf-8") as fh:
    episode_template_html = fh.read()
with open(serie_template_file, "r", encoding="utf-8") as fh:
    serie_template_html = fh.read()
with open(tag_template_file, "r", encoding="utf-8") as fh:
    tag_template_html = fh.read()

# Load configuration and data files
with open(config_data_file, "r", encoding="utf-8") as fh:
    config = yaml.safe_load(fh)
with open(episodes_data_file, "r", encoding="utf-8") as fh:
    all_episodes = yaml.safe_load(fh)
    episodes = []
    for episode in all_episodes:
        episode["tags"].sort(key=str.lower)
        if episode["published"]:
            episodes.append(episode)
    episodes.reverse()
with open(platforms_data_tile, "r", encoding="utf-8") as fh:
    platforms = yaml.safe_load(fh)

# Initialize Jinja2 environment with custom filters
env = Environment()
env.filters["slugify"] = slugify

# Build tag index for related episode discovery
tags = {}
for episode in episodes:
    if not episode["published"]:
        continue
    for tag in episode["tags"]:
        if tag not in tags:
            tags[tag] = []
        tags[tag].append(episode["id"])


def build_menu_html(title=None, link=None, items=None):
    """Generate HTML menu item(s) from navigation configuration.

    Creates either a simple link item or a dropdown menu with nested items. Special handling
    for the "Episodi" (Episodes) menu item to append series submenu.

    Args:
        title (str, optional): Menu item title/label
        link (str, optional): URL for simple link items
        items (list, optional): List of dicts with 'link' and 'title' keys for dropdown items

    Returns:
        str: HTML markup for menu item(s) with appropriate structure and CSS classes
    """
    output_html = ''
    if link:
        output_html = f'<li><a href="{link}">{title}</a></li>'
    if items:
        output_html = f'<li class="has-children"><a href="#">{title}</a><ul class="dropdown arrow-top">'
        for item in items:
            output_html += f'<li><a href="{item["link"]}">{item["title"]}</a></li>'
        output_html += '</ul></li>'
    if title == "Episodi":
        title = "Serie"
        output_html += f'<li class="has-children"><a href="#">{title}</a><ul class="dropdown arrow-top">'
        for serie_id, serie in config["series"].items():
            output_html += (
                f'<li><a href="/series/{serie_id}.html">{serie["title"]}</a></li>'
            )
        output_html += '</ul></li>'
    return output_html
for menu in config["menu"]:
    menu_html += build_menu_html(**menu)
menu_html += '</ul></nav></div>'

# ==============================================================================
# RENDER MAIN LANDING PAGE
# ==============================================================================
main_template = env.from_string(main_template_html)
main_html = main_template.render(
    config=config, menu=menu_html, episodes=episodes, platforms=platforms
)
with open("index.html", "w", encoding="utf-8") as fh:
    fh.write(main_html)


# ==============================================================================
# RENDER EPISODE INDEX PAGE
# ==============================================================================
os.makedirs("episodes", exist_ok=True)
episode_index_template = env.from_string(episode_index_template_html)
episode_index_html = episode_index_template.render(
    config=config, menu=menu_html, episodes=episodes
)
with open("episodes/index.html", "w", encoding="utf-8") as fh:
    fh.write(episode_index_html)


# ==============================================================================
# RENDER INDIVIDUAL EPISODE PAGES
# ==============================================================================
episode_template = env.from_string(episode_template_html)
reversed_episodes = list(episodes)
reversed_episodes.reverse()
for episode in reversed_episodes:
    if not episode["published"]:
        continue

    # Load markdown transcript if available
    transcript_file = f"transcripts/episode-{episode['id']}.md"
    transcript = None
    if os.path.exists(transcript_file):
        with open(transcript_file, "r") as fh:
            transcript = markdown.markdown(fh.read())

    # Discover related episodes via shared tags
    related_ids = []
    related = []
    for tag in episode["tags"]:
        if tag not in config["tags"]:
            print(
                f"WARNING: tag {tag} in episode {episode['id']} is not in the primary list"
            )
        for related_id in tags[tag]:
            if related_id == episode["id"]:
                continue
            if related_id not in related_ids:
                related_ids.append(related_id)
                for related_episode in episodes:
                    if related_episode["id"] == related_id:
                        related.append(related_episode)

    episode_html = episode_template.render(
        config=config,
        menu=menu_html,
        episode=episode,
        platforms=platforms,
        related=related,
        transcript=transcript,
    )

    with open(f"episodes/episode-{episode['id']}.html", "w", encoding="utf-8") as fh:
        fh.write(episode_html)


# ==============================================================================
# RENDER TAG-BASED EPISODE COLLECTION PAGES
# ==============================================================================
os.makedirs("tags", exist_ok=True)
tag_template = env.from_string(tag_template_html)
for tag, related_ids in tags.items():
    slug = slugify(tag)

    related = []
    for related_episode in episodes:
        if related_episode["id"] in related_ids:
            related.append(related_episode)

    tag_html = tag_template.render(
        config=config, menu=menu_html, tag=tag, related=related
    )
    with open(f"tags/tag-{slug}.html", "w", encoding="utf-8") as fh:
        fh.write(tag_html)


# ==============================================================================
# RENDER SERIES/CATEGORY PAGES
# ==============================================================================
os.makedirs("series", exist_ok=True)
serie_template = env.from_string(serie_template_html)
for serie_id, serie in config["series"].items():
    slug = slugify(serie_id)
    sections = []
    for section in serie.get("sections", []):
        related_episodes = []
        section_episodes = section.get("episodes", [])
        section_episodes.sort()
        for related_episode_id in section_episodes:
            for episode in episodes:
                if episode["id"] == related_episode_id:
                    related_episodes.append(episode)
        if related_episodes:
            sections.append(
                {
                    "title": section.get("title"),
                    "episodes": related_episodes,
                }
            )
    serie_html = serie_template.render(
        config=config, menu=menu_html, serie=serie, sections=sections
    )
    with open(f"series/{slug}.html", "w", encoding="utf-8") as fh:
        fh.write(serie_html)


# ==============================================================================
# PERSIST UPDATED CONFIGURATION FILES
# ==============================================================================
with open("config/config.yaml", "w", encoding="utf-8") as fh:
    yaml.dump(
        config,
        fh,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=True,
        indent=2,
    )
with open("config/episodes.yaml", "w", encoding="utf-8") as fh:
    yaml.dump(
        all_episodes,
        fh,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=True,
        indent=2,
    )

