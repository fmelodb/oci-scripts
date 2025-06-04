# Language: PT-BR
# Código: Python
# Tabela de exemplo:  source_tab (id integer, data json)
# Objetivo: Atualizar o TTL de cada linha para 3 dias (o código se aplica a qualquer tipo de update, já que multi-row update não é suportado)

from borneo import NoSQLHandle, NoSQLHandleConfig, Regions, QueryRequest, PrepareRequest
from borneo.iam import SignatureProvider

handleConfig = NoSQLHandleConfig(Regions.US_ASHBURN_1)
config = handleConfig.set_authorization_provider(SignatureProvider())
config.set_default_compartment('fmelo')
handler = NoSQLHandle(config)

select_statement = 'select id from source_tab'
update_statement = 'declare $vId integer; update source_tab set ttl 3 days where id=$vId'

request = QueryRequest().set_statement(select_statement)
prepRequest = PrepareRequest().set_statement(update_statement)
prepStmt = handler.prepare(prepRequest).get_prepared_statement()

while True:
    result = handler.query(request)
    for r in result.get_results():
        prepStmt.set_variable('$vId', r['id'])
        updateRequest = QueryRequest().set_prepared_statement(prepStmt)
        handler.query(updateRequest)
    if request.is_done():
        break
