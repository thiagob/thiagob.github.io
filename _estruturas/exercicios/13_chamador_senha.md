---
layout: page
title: Chamador de Senha
category: exercicio
subject: Listas Lineares
lesson: 5
---


Uma operadora de telefonia celular montou uma nova loja com 1 balcões de atendimento.
Para atender os clientes que chegam a loja foi implementado um gerenciador de fila / chamador de senha de acordo com as seguintes regras:

1. Se ninguém estiver sendo antendido, quando uma pessoa chega na loja ela pode ir diretamente para o balcão.
1. Cada atendimento dura sempre 3 minutos. Quando o antedimento é concluído, o antendente chama o próximo cliente no minuto seguinte.

**Por exemplo:**
```
Minuto 1: João chega na loja e vai ao balcão. Seu antendimento começa imediatamente.
Minuto 2: João está sendo atendido, enquanto José chega a loja.
Minuto 3: O antendimento de João é concluído.
Minuto 4: José vai ao balcão e seu atendimento começa.
Minuto 5: José está sendo atendido.
Minuto 6: O antendimento de José concluído
Minuto 7: Atendente aguarda, pois não há ninguém para ser atendido.
Minuto 8: Maria chega na loja, vai ao balcão e seu atendimento começa.
```

