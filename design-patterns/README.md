# Python Design Patterns

The purpose of this project is to document my coding practices for the book:  Practical Python Design Patterns by Wessel Badenhorsof. All design patterns are divided into three categories (directories): **Creational**, **Structural** & **Behavioural**. Each pattern is contained within its own module (with its own `.py` script). Each module contains a sample implementation along with some demonstrative tests and extensive documentation.

Each module can be run as a standalone python script or imported into other scripts, some of them will need the requierements, I would recomend to install virtual enviroment and install there with:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requeriments.txt   //Instala dependencias

Please feel free to suggest modifications/updates.

## Index

+ [**Creational Patterns**](./creational) (4/5 Done)
    + [Singleton](./creational/singleton.py) - Done!
    + [Prototype](./creational/prototype.py) - Done!
    + [Factory](./creational/factory.py) - Done!
    + [Builder](./creational/builder.py) - Done!
    + [Pool](./creational/pool.py)

+ [**Structural Patterns**](./structural) (0/6 Done)
    + [Pythonesque Decorator](./structural/pythonesque_decorator.py)
    + [Facade](./structural/facade.py)
    + [Proxy](./structural/proxy.py)
    + [Flyweight](./structural/flyweight.py)
    + [Adapter](./structural/adapter.py)
    + [Composite](./structural/composite.py)

+ [**Behavioural Patterns**](./behavioural) (0/7 Done)
    + [Chain of Responsibility](./behavioural/chain_of_responsibility.py)
    + [Mediator](./behavioural/mediator.py)
    + [Observer](./behavioural/observer.py)
    + [Command](./behavioural/command.py)
    + [Memento](./behavioural/memento.py)
    + [Registry](./behavioural/registry.py)
    + [Strategy](./behavioural/strategy.py)

I clone original repository from: **prateeksan** but i intended to replace all code from it to practices every pattern
Thanks man for your public repo, it help me to start with this...