# Role Ansible para Ubuntu

## Ajustes

Editar o arquio group_vars/all com os seguintes valores

```python

# Usuario para acesso e login no rabbitmq manager
admin_user: admin
admin_password: admin

# Erlang Cookie - Todos os nodes devem ter o mesmo cookie para
# formarem um cluster
erlang_cookie: PZCYRTAWOOCGDYDUIBZX

# Hipe Compile - High performance Erlang
# para melhorar o throughput e tempo de startup time.
hipe_compile: true|false

# WaterMark - Valor (em porcentagem) da quantidade de uso de memória para o rabbitmq.
watermark: 0.62

# Master - Necessário definir quem é o master para o seutp do cluster
# Colocar o ansible inventory hostname para ignorar etapas que não sejam do master
rabbitmq_master: rabbitmq-master
```

## Plugins

Dentro de plugins temos um diretório chamado stress com um simples python para alimentar e consumir as filas.
