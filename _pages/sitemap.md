---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

<ul>
  <li><a href="{{ base_path }}/">Bio</a></li>
  {% for item in site.data.navigation.main %}
  <li><a href="{{ base_path }}{{ item.url }}">{{ item.title }}</a></li>
  {% endfor %}
</ul>

An [XML sitemap]({{ '/sitemap.xml' | relative_url }}) is also available.
