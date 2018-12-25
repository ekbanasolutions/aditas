from src.json2xml import Json2xml

static_xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n' \
                     '<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n' \
                     '<!--\n' \
                     '  Licensed under the Apache License, Version 2.0 (the "License");\n' \
                     '  you may not use this file except in compliance with the License.\n' \
                     '  You may obtain a copy of the License at\n\n' \
                     '      http://www.apache.org/licenses/LICENSE-2.0\n\n' \
                     '  Unless required by applicable law or agreed to in writing, software\n' \
                     '  distributed under the License is distributed on an "AS IS" BASIS,\n' \
                     '  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n' \
                     '  See the License for the specific language governing permissions and\n' \
                     '  limitations under the License. See accompanying LICENSE file.\n' \
                     '-->\n\n'


# Returns xml configuration from loaded json
def get_xml_configuration(final_content):
    '''
    :param final_content: json configuration
    :return: Returns xml configuration
    '''
    conf = {}
    conf_lst = []
    for data in final_content:
        conf_inner = {}
        name = data
        value = final_content[data]
        conf_inner['name'] = name
        conf_inner['value'] = value
        conf_lst.append(conf_inner)
    conf['property'] = conf_lst
    data_object = Json2xml(conf)
    conf_xml = data_object.json2xml()
    conf_xml = conf_xml.replace('<all>', '<configuration>')
    conf_xml = conf_xml.replace('</all>', '</configuration>')
    final_configuration = static_xml_content + conf_xml
    return final_configuration


# Returns yml configuration from loaded json
def get_yml_configuration(final_content):
    '''
    :param final_content: json configuration
    :return: Returns yml configuration
    '''
    final_configuration = ""
    for data in final_content:
        name = data
        value = final_content[name]
        final_configuration = final_configuration + "%s: %s\n" % (name, value)

    return final_configuration


# Returns conf or cfg or sh configuration from loaded json
def get_conf_cfg_sh_configuration(final_content):
    '''
    :param final_content: json configuration
    :return: Returns {key=value} format configuration
    '''
    final_configuration = ""
    for data in final_content:
        name = data
        value = final_content[name]
        final_configuration = final_configuration + "%s=%s\n" % (name, value)

    return final_configuration
