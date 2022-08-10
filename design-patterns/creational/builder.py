""" The Builder Pattern

Notes:

The Builder Pattern is particularly useful for creating complex objects made up of
several smaller objects. This pattern uses classes to represent both objects and their
builders (used to assemble objects). By having all child builders inherit from an
abstract builder, it is possible to place restrictions on the implementations of all
child builders by changing code in just the abstract builder class. Furthermore, allowing
only director objects to use the builders ensures control over object creation (similar
to the Factory Pattern). 

"""
# Python Imports
import tempfile
import webbrowser
from abc import ABCMeta, abstractmethod
from http.server import BaseHTTPRequestHandler, HTTPServer

# Personal Imports
from singleton import Logger

# Instance Logger
logging = Logger("builder.log")

# Classes Definition
class AbstractDirector(object, metaclass=ABCMeta):
    ''' The director only knows how to use the builder and return the product'''
    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder # Super generic, Any AbstractFormBuilder could be used

    @abstractmethod
    def construct(self, config, field_list):
        # In the real classes we will define what we need here
        pass
    
    def get_constructed_object(self):
        return self._builder.constructed_object

class AbstractFormBuilder(object, metaclass=ABCMeta):
    ''' 
        The Builder is attached to the director and knows the specific
        The idea is be able to create different Builders for different situations
        Always knowing that the director.construct() will work
    '''
    def __init__(self):
        self.constructed_object = None
    
    @abstractmethod
    def configure_form(self, config):
        pass
    
    @abstractmethod
    def add_text_field(self, field_dict):
        pass
    
    @abstractmethod
    def add_checkbox(self, checkbox_dict):
        pass

    @abstractmethod
    def add_radiogroup(self, radio_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass

# Builders:
class HtmlForm(object):
    def __init__(self):
        self.form_attrs = ""
        self.field_list = []

    def __repr__(self):
        return "<form {0}>{1}</form>".format(
            self.form_attrs,
            "".join(self.field_list)
        )

class FormDirector(AbstractDirector):
    def __init__(self):
        AbstractDirector.__init__(self)

    def construct(self, config, field_list):
        # Set form
        self._builder.configure_form(config)
        # Set fields
        for field in field_list:
            if field["field_type"] == "text_field":
                self._builder.add_text_field(field)
            elif field["field_type"] == "checkbox":
                self._builder.add_checkbox(field)
            elif field["field_type"] == "radio_group":
                self._builder.add_radiogroup(field)
            elif field["field_type"] == "button":
                self._builder.add_button(field)    

class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object = HtmlForm() # At this point is empty
    
    def configure_form(self, config):
        self.form_attrs = " ".join(
            [f'{key}="{value}"' for key,value in config.items()]
        )
    
    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            '{0}:<br><input type="text" name="{1}"><br>'.
            format(
                field_dict['label'],
                field_dict['field_name']
            )
        )
    
    def add_checkbox(self, checkbox_dict):
        self.constructed_object.field_list.append(
            '<label><input type="checkbox" id="{0}" value="{1}"> {2}<br></label>'.
            format(
                checkbox_dict['field_id'],
                checkbox_dict['value'],
                checkbox_dict['label']
            )
        )

    def add_radiogroup(self, radio_dict):
        self.constructed_object.field_list.append(
            "<fieldset>{0}{1}</fieldset>".format( # Main Block
                # Legend
                '<legend>{0}</legend>'.format(radio_dict["label"]),
                # every value is a item
                "".join(
                    [
                        '<label><input type="radio" name="{0}" value="{1}"> {2}</label>'
                        .format(
                            radio_dict["field_name"],
                            value["value"],
                            value["label"]
                        )
                        for value in radio_dict['values'] # List compression to generate every radio item
                    ]
                )
            )
        )

    def add_button(self, button_dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.
            format(
                button_dict['text']
            )
        )   

def generate_form():
    # Instance Director and Builder
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)
    # Define Fields
    config = {
        'action':'',
        'method':'post',
    }
    field_list = [
        {
            "field_type": "text_field",
            "label": "Put some text here",
            "field_name": "FieldOne"
        },
        {
            "field_type": "checkbox",
            "field_id": "check_it",
            "value": "1",
            "label": "CheckBox",
        },
        {
            "field_type": "radio_group",
            "field_name": "pickone",
            "label": "Pick One",
            "values": [
                {"value": 1, "label": "Option 1"},
                {"value": 2, "label": "Option 2"},
                {"value": 3, "label": "Option 3"},
            ]
        },
        {
            "field_type": "button",
            "text": "Submit"
        }
    ]
    director.construct(config, field_list)
    return "<html><body>{0!r}</body></html>".format(
        director.get_constructed_object()
    )


# Define Server
class CustomServer(BaseHTTPRequestHandler):      
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self): # In this case we treat any path the same
        logging.info(
            "GET request,\nPath: {0}\nHeaders:\n{1}\n".format(
                self.path,
                self.headers
            )
        )
        self._set_response()
        # response:
        self.wfile.write(generate_form().encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info(
            "POST request,\nPath: {0}\nHeaders:\n{1}\n\nBody:\n{2}\n".format(
                self.path,
                self.headers,
                post_data.decode('utf-8')
            )
        )
        # Prepare Response
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run_server(server_class=HTTPServer, handler_class=CustomServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

# Execution
if __name__ == "__main__":
    # Run Server
    run_server()