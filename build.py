#!/usr/bin/env python3

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

if os.path.exists("episodes"):
    shutil.rmtree("episodes")
if os.path.exists("tags"):
    shutil.rmtree("tags")
if os.path.exists("series"):
    shutil.rmtree("series")

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

# Jinja environment
env = Environment()
env.filters["slugify"] = slugify

# Read tags
tags = {}
for episode in episodes:
    if not episode["published"]:
        continue
    for tag in episode["tags"]:
        if tag not in tags:
            tags[tag] = []
        tags[tag].append(episode["id"])


# Build menu
def build_menu_html(title=None, link=None, items=None):
    output_html = ''
    if link:
        output_html = f'<li><a href="{link}">{title}</a></li>'
    if items:
        output_html = f'<li class="has-children"><a href="#">{title}</a><ul class="dropdown arrow-top">'
        for item in items:
            output_html += f'<li><a href="{item["link"]}">{item["title"]}</a></li>'
        output_html += '</ul></li>'
    return output_html


menu_html = '<div class="col-9" data-aos="fade-down"><nav class="site-navigation position-relative text-right text-md-right" role="navigation"><div class="d-inline-block ml-md-0 mr-auto py-3"><a href="#" class="site-menu-toggle js-menu-toggle text-white"><span class="icon-menu h3"></span></a></div><ul class="site-menu js-clone-nav d-none">'
for menu in config["menu"]:
    menu_html += build_menu_html(**menu)
menu_html += '</ul></nav></div>'

# Main page
main_template = env.from_string(main_template_html)
main_html = main_template.render(
    config=config, menu=menu_html, episodes=episodes, platforms=platforms
)
with open("index.html", "w", encoding="utf-8") as fh:
    fh.write(main_html)


# Episode index page
os.makedirs("episodes", exist_ok=True)
episode_index_template = env.from_string(episode_index_template_html)
episode_index_html = episode_index_template.render(
    config=config, menu=menu_html, episodes=episodes
)
with open("episodes/index.html", "w", encoding="utf-8") as fh:
    fh.write(episode_index_html)


# Per episode page
episode_template = env.from_string(episode_template_html)
reversed_episodes = list(episodes)
reversed_episodes.reverse()
for episode in reversed_episodes:
    if not episode["published"]:
        continue

    # Transcript
    transcript_file = f"transcripts/episode-{episode['id']}.md"
    transcript = None
    if os.path.exists(transcript_file):
        with open(transcript_file, "r") as fh:
            transcript = markdown.markdown(fh.read())

    # Find related episodes
    related_ids = []
    related = []
    for tag in episode["tags"]:
        if tag not in config["tags"]:
            print(
                f"WARNING: tag {tag} in episode {episode['id']} is not in the primary list"
            )
        for related_id in tags[tag]:
            if related_id == episode["id"]:
                # Skip same episode
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


# Tags
os.makedirs("tags", exist_ok=True)
tag_template = env.from_string(tag_template_html)
for tag, related_ids in tags.items():
    slug = slugify(tag)

    # Find related episodes
    related = []
    for related_episode in episodes:
        if related_episode["id"] in related_ids:
            related.append(related_episode)

    tag_html = tag_template.render(
        config=config, menu=menu_html, tag=tag, related=related
    )
    with open(f"tags/tag-{slug}.html", "w", encoding="utf-8") as fh:
        fh.write(tag_html)


# Series page
os.makedirs("series", exist_ok=True)
serie_template = env.from_string(serie_template_html)
for serie_id, serie in config["series"].items():
    slug = slugify(serie_id)
    sections = []
    for section in serie["sections"]:
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
                    "title": section["title"],
                    "episodes": related_episodes,
                }
            )
    serie_html = serie_template.render(
        config=config, menu=menu_html, serie=serie, sections=sections
    )
    with open(f"series/{slug}.html", "w", encoding="utf-8") as fh:
        fh.write(serie_html)


# Update config files
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
