from django.db import models
from datetime import datetime
from django.utils.timezone import now

class ClientUser(models.Model):
    class EstadoChoice(models.TextChoices):
        Acre = 'Acre (AC)'
        Alagoas = 'Alagoas (AL)'
        Amapa = 'Amapá (AP)'
        Amazonas = 'Amazonas (AM)'
        Bahia = 'Bahia (BA)'
        Ceara = 'Ceará (CE)'
        Distrito_Federal = 'Distrito Federal (DF)'
        Espirito_Santo = 'Espírito Santo (ES)'
        Goias = 'Goiás (GO)'
        Maranhao = 'Maranhão (MA)'
        Mato_Grosso = 'Mato Grosso (MT)'
        Mato_Grosso_do_Sul = 'Mato Grosso do Sul (MS)'
        Minas_Gerais = 'Minas Gerais (MG)'
        Para = 'Pará (PA)'
        Paraiba = 'Paraíba (PB)'
        Parana = 'Paraná (PR)'
        Pernambuco = 'Pernambuco (PE)'
        Piaui = 'Piauí (PI)'
        Rio_de_Janeiro = 'Rio de Janeiro (RJ)'
        Rio_Grande_do_Norte = 'Rio Grande do Norte (RN)'
        Rio_Grande_do_Sul = 'Rio Grande do Sul (RS)'
        Rondonia = 'Rondônia (RO)'
        Roraima = 'Roraima (RR)'
        Santa_Catarina = 'Santa Catarina (SC)'
        Sao_Paulo = 'São Paulo (SP)'
        Sergipe = 'Sergipe (SE)'
        Tocantins = 'Tocantins (TO)'