## Lanchonete Django
Estava sem muito o que fazer, decidi criar um sistema para uma lanchonete.  
O sitema permite registrar ingredientes, registrar bebidas, criar lanches e anotar pedidos.  

## Rotas
#### Rota para paginas
**URL dashboard:** 127.0.0.1/admin  
**URL home-page:**  127.0.0.1/home   
**URL menu de ingredientes:** 127.0.0.1/ingredient/menu  
**URL adição de ingredientes:**  127.0.0.1/ingredient/create  
**URL listagem de ingredientes:**  127.0.0.1/ingredient/list  
**URL filtragem de ingredientes:**  127.0.0.1/ingredient/filter  
**URL edição de ingredientes:**  127.0.0.1/ingredient/edit/<int:id>    
**URL menu de lanches:**  127.0.0.1/sandwich/menu  
**URL criaçao de lanches:** 127.0.0.1/sandwich/create  
**URL listagem de lanches:** 127.0.0.1/sandwich/list  
**URL editar de lanche:** 127.0.0.1/sandwich/edit/<int:id>    
**URL filtragem de lanches:**  127.0.0.1/sandwich/filter  
**URL adicionar nova bebida:**  127.0.0.1/beverage/create  
**URL listagem de bebida:**  127.0.0.1/beverage/list   
**URL filtragem de bebida:**  127.0.0.1/beverage/filter  

#### Rotas para Rest  
**URL adição de ingredientes:**  127.0.0.1/ingredient/create/submit  
**URL filtragem de ingredientes:**  127.0.0.1/ingredient/filter/submit  
**URL edição de ingredientes:**  127.0.0.1/ingredient/edit/submit  
**URL criaçao de lanches:** 127.0.0.1/sandwich/create/submit  
**URL editar de lanche:** 127.0.0.1/sandwich/edit/submit  
**URL remover ingrediente do lanche:** 127.0.0.1/sandwich/remove/<int:sandwich_id>/<int:ingredient_id>  
**URL filtragem de lanches:**  127.0.0.1/sandwich/filter/submit   
**URL adicionar nova bebida:**  127.0.0.1/beverage/create/submit   
**URL filtragem de bebida:**  127.0.0.1/beverage/filter/submit   


## Tarefas  
- [X] Criar header e page models  
- [X] Criar testes para template  
- [X] Adicionar o Bootstrap  
- [X] Adicionar o Fontawesome 
- [X] Criar modelos do banco de dados.  
- [X] Testes templates  ingredientes  
- [X] Testes para models ingredientes  
- [X] Menu de ingredientes  
- [X] Tela para listar ingredientes  
- [X] Tela para filtrar ingredientes  
- [X] Tela para cadastrar ingredientes  
- [X] Tela para atualizar ingredientes 
- [X] Testes templates  lanches  
- [X] Testes para models lanches  
- [X] Menu de lanches  
- [X] Tela para listar lanches  
- [X] Tela para filtrar lanches  
- [X] Tela para cadastrar lanches  
- [X] Tela para atualizar lanches  
- [X] Testes templates  bebidas  
- [X] Testes para models bebidas  
- [X] Menu de bebidas  
- [X] Tela para listar bebidas  
- [X] Tela para filtrar bebidas  
- [X] Tela para cadastrar  
- [X] Tela para atualizar bebidas  
- [ ] Testes templates  pedido  
- [ ] Testes para models pedido  
- [ ] Menu de pedido  
- [ ] Realizar um pedido  
- [ ] Atualizar um pedido  
- [ ] Finalizar um pedido     

## Banco de dados  
#### Vi alguns erros no banco, deixar assim por enquanto
![image](https://user-images.githubusercontent.com/56879793/98428575-ec762300-2080-11eb-87cc-74fd8de9081f.png)
 
