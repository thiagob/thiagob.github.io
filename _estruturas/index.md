---
layout: page
title: Estruturas Avançadas de Dados
permalink: /estruturas/
---

# Turmas

* [IENH 2022/1](https://classroom.google.com/u/1/c/NDYxNTEyODMzMzEw)


# Exercícios

{% assign items = site.estruturas | where:"category","exercicio" %}
<ol>
  {% assign subject = '' %}
  {% for item in items limit:33 %}
    {% if subject != item.subject %}
      {% assign subject = item.subject %}
      <h2>{{ item.subject }}</h2>
    {% endif %}
  
    <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
  {% endfor %}
</ol>


