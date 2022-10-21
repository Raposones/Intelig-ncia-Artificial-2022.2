# Inteligência Artificial - 2022.2

## Atividade - Mapa da Romênia - Busca Heurística - Gulosa/A*

### Descrição
A atividade é baseada em um mapa rodoviário do país da Romênia:
<br>

![map](images/romania_map.png)

<br>

Dado o mapa, pede-se que seja feita uma **busca heurística** para achar a distância total entre um dado estado (dito por um input do usuário) e o estado de Bucareste (*Bucharest*), bem como o caminho completo (todos os estados percorridos no processo). Para efeitos de imaginação, supomos que um usuário irá viajar de ônibus de algum estado para Bucareste, e deseja saber o caminho e a distância que irá percorrer.

<br>

### Objetivo
O objetivo da atividade é apenas mostrar o caminho percorrido e a distância total entre um estado e Bucareste, por meio de uma **busca heurística**. <br>
Para essa busca, temos um tipo de dado adicional: a distância de cada cidade até a cidade alvo (Bucareste), **em linha reta**. Os dados são os seguintes:
<br>
![data](images/h_dist.png)
<br>
Baseado nesses dados, utilizamos os seguintes métodos de busca:

1. **Busca Gulosa**: a busca é baseada apenas na distância em linha reta. <br> Ou seja, dado um estado, ele irá percorrer os estados com a menor distância **em linha reta** até Bucareste.

2. **Busca A***: esta busca é similar à anterior, adicionalmente considerando a distância de um estado até o primeiro estado dado.
Ou seja, a fórmula considerada aqui é <br> __*distância em linha reta* + *distância do estado atual do estado inicial*__<br>
O estado que tiver o menor valor nesta fórmula é escolhido para ser percorrido.

<br>

### Imagens

* Exemplo: **Arad** como estado inicial

<br>

![arad](images/arad_example.png)

<hr>
<br>

* Exemplo: **Neamt** como estado inicial

<br>


![neamt](images/neamt_example.png)

<hr>
<br>

* Exemplo: **Mehadia** como estado inicial

<br>

![mehadia](images/mehadia_example.png)

<hr>
<br>

* Exemplo: **Zerind** como estado inicial

<br>

![mehadia](images/zerind_example.png)

<hr>
<br>




* <span style="color:red">**ERRO**</span>: **Bucharest** como estado inicial - não se pode viajar para um estado se você já está nele!

<br>

![error1_alreadyin](images/already_in_state.png)

<hr>
<br>

* <span style="color:red">**ERRO**</span>: Estado inicial inválido - não existe ou não é um estado da Romênia.

<br>

![error2_notvalid](images/not_state.png)

<br>