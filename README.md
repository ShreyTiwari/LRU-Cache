# LRU-Cache

### Introduction
The <i>'Least Recently Used'</i> or simply the <i>LRU Cache Eviction Policy</i> is a widely used policy in the modern computer science world.
This repository provides an implementation of the LRU Cache using the <b>Linked List</b> and <b>Hashmap</b> approach. The <b>Space Complexity</b> 
of the implementation is <b>O(n)</b> and the <b>time complexity</b> is <b>O(1)</b>.<br />

However, this repository also inculcates common <b>Corporate Software Development</b> practices in the code. A few are listed below:
- Code Versioning
- Modularization
- Error Handling (Input Verification)
- Unit Testing* (Under Development)
- Logging
- Documentation

Note: The code aims to provide an introduction to the mentioned above topics and not an <i>overkill</i> implementation of the LRU Cache.

### Code Structure
The code in this repository is structured into modules. Here is a brief description on the code base:
- <b>LRU_Cache.py</b>: The main file to interact with the LRU Cache implementation logic.
- <b>Linked_List</b>: Folder containing the implementation of the Doubly Linked List used by the LRU Cache.
- <b>Helper</b>: Folder containing the implementation of common functions that can be shared across different modules.
- <b>Logger</b>: Folder containing the implementation of a wrapper over the standard Python logging module.

### Usage
All the modules can be run independently for testing and understanding purposes. If you are 
using a text editors like Visual Studio Code or Pycharm, you can run the modules directly. To use the command line 
for program execution, use the following command:

```python3 <filename>.py```

### References
- Linked List implementation in Python:
  - https://www.geeksforgeeks.org/linked-list-set-1-introduction/
- Implementing LRU cache:
  - https://www.youtube.com/watch?v=akFRa58Svug&ab_channel=TECHDOSE
- Python Logging:
  - https://docs.python.org/3/howto/logging.html
  - https://www.youtube.com/watch?v=g8nQ90Hk328&ab_channel=Socratica