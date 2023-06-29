import zeep
import asyncio


class ConsultaCepCorreioService():

    def __init__(self, cep):
        self.cep = cep

    async def consulta_cep_async(self):
        try: 
            wsdl = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
            client = zeep.AsyncClient(wsdl=wsdl)
            res = await client.service.consultaCEP(self.cep)   
            return res
                
        except Exception as error:
            return error    
    
    def get_dados_async(self):
        dados = asyncio.run(self.consulta_cep_async())
        return dados





