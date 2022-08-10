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

# Classes Definition
class AbstractDirector(object, metaclass=ABCMeta):
    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, field_list):
        pass
    
    def get_constructed_object(self):
        return self._builder.constructed_object

class AbstractFormBuilder(object, metaclass=ABCMeta):
    def __init__(self):
        self.constructed_object = None
    
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
        self.field_list = []

    def __repr__(self):
        return "<form>{}</form>".format("".join(self.field_list))

class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object = HtmlForm()
    
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
            '<label><input type="checkbox" id="{0}" value="{1}"> {2}<br>'.
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
            

class FormDirector(AbstractDirector):
    def __init__(self):
        AbstractDirector.__init__(self)

    def construct(self, field_list):
        for field in field_list:
            if field["field_type"] == "text_field":
                self._builder.add_text_field(field)
            elif field["field_type"] == "checkbox":
                self._builder.add_checkbox(field)
            elif field["field_type"] == "radio_group":
                self._builder.add_radiogroup(field)
            elif field["field_type"] == "button":
                self._builder.add_button(field)       
 
# Execution
if __name__ == "__main__":
    director = FormDirector()
    # Define Fields
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
            "text": "DONE"
        }
    ]
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)
    director.construct(field_list)
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
        url = 'file://' + f.name
        f.write(
            "<html><body>{0!r}</body></html>".
                format(
                    director.get_constructed_object()
                )
        )
        webbrowser.open(url)