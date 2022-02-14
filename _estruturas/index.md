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
  {% for item in items limit:33 %}
    <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
  {% endfor %}
</ol>


