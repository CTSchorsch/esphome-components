import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import CONF_ID

DEPENDENCIES = ['uart']

AUTO_LOAD = ['sensor']

mspawifi_ns = cg.esphome_ns.namespace('mspawifi')

MSPAWifi = mspawifi_ns.class_('MSPAWifi', cg.Component)

CONF_REMOTE_UART = "remote_uart"
CONF_POOL_UART = "pool_uart"
CONF_ACTTEMP = "act_temp"

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(MSPAWifi),
    cv.Optional(CONF_REMOTE_UART): cv.use_id(uart.UARTComponent),
    cv.Optional(CONF_POOL_UART): cv.use_id(uart.UARTComponent),
    cv.Optional(CONF_ACTTEMP): sensor.sensor_schema(
        accuracy_decimals = 1
    ),
})


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if CONF_REMOTE_UART in config:
        remote_uart = await cg.get_variable(config[CONF_REMOTE_UART])
        cg.add(var.set_remote_uart(remote_uart))
    if CONF_POOL_UART in config:
        pool_uart = await cg.get_variable(config[CONF_POOL_UART])
        cg.add(var.set_pool_uart(pool_uart))
    if CONF_ACTTEMP in config:
        sens = await sensor.new_sensor(config[CONF_ACTTEMP])
        cg.add(var.set_acttemp_sensor(sens))

