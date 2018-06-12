CLUSTER bairro USING idx_bairro_descricao;
CLUSTER bairro USING idx_bairro_codigo;
CLUSTER endereco USING idx_logradouro;
VACUUM endereco;
VACUUM bairro;


REINDEX TABLE endereco;
REINDEX TABLE bairro;
REINDEX INDEX idx_bairro_descricao;
REINDEX INDEX idx_logradouro;
REINDEX INDEX idx_bairro_codigo;
REINDEX INDEX idx_endereco_bairro_codigo;

SELECT bairro.bairro_descricao, endereco.endereco_logradouro FROM endereco JOIN bairro 
ON endereco.bairro_codigo = bairro.bairro_codigo WHERE endereco.endereco_logradouro LIKE 'B%';

LOG:  duration: 110.295 ms




SELECT * FROM endereco WHERE endereco_cep = '72404901';
SELECT * FROM endereco WHERE endereco_logradouro LIKE '%A'; 


SELECT bairro.bairro_descricao, endereco.endereco_logradouro FROM bairro JOIN endereco 
ON bairro.bairro_codigo = endereco.bairro_codigo ORDER BY bairro.bairro_descricao DESC;








LOG:  duration: 942.228 ms 
