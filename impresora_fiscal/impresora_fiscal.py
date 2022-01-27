# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
from odoo.tools import ustr

# Impresora Fiscal:
import sys
from . import Tfhka
# from . import serial
import os
import time


class ImpresoraFiscal(models.Model):
    """Funcionalidades de la Impresora Fiscal BIXOLON812."""
    _name = "impresora.fiscal"
    _description = 'Impresora Fiscal'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Descripción', required=True, index=True)
    puerto = fields.Integer(string='Puerto', required=True)
    activo = fields.Boolean(string='Activo', default=True)

    # Comprobar conexión:
    '''
    def probar_conexion(self):
        try:
            puerto = "COM4"
            printer = Tfhka.Tfhka()
            try:
                resp = printer.OpenFpctrl(puerto)
                if resp == False:
                    raise UserError(
                        _('Impresora no Conectada o Error Accediendo al Puerto - 1'))
            except:
                raise UserError(
                    _('Impresora no Conectada o Error Accediendo al Puerto - 2'))                
        except serial.SerialException as e:
            raise UserError(
                _("Impresora no Conectada o Error Accediendo al Puerto. - 3", ustr(e)))

        message = _("Connection Test Successful!")
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': False,
            }
        }
    '''

    def documentoNF(self):
        printer = Tfhka.Tfhka()
        printer.PrintXReport()
        '''
        resp = printer.SendCmd("D")
        try:
            if resp == False:
                raise UserError(
                    _('Error al ejecutar función - 1'))
        except serial.SerialException as e:
            raise UserError(
                _("Error al ejecutar función - 2", ustr(e)))

        message = _("Función ejecutada correctamente")
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': False,
            }
        }        
        '''

        # respuesta = printer.SendCmd(str("I0X"))
        # return {
        #     'type': 'ir.actions.client',
        #     'tag': 'display_notification',
        #     'params': {
        #         'message': respuesta,
        #         'type': 'success',
        #         'sticky': False,
        #     }
        # }        
