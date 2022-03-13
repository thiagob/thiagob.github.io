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
  {% assign lesson = 0 %}
  
  {% for item in items limit:33 %}
    <li>
      {% if subject != item.subject %}
        {% assign subject = item.subject %}
        <h3>{{ item.subject }}</h3>
      {% endif %}
      {% if lesson != item.lesson %}
        {% assign lesson = item.lesson %}
        <h3>{{ item.lesson }}</h3>
      {% endif %}
  
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
  </li>
  {% endfor %}
</ol>


