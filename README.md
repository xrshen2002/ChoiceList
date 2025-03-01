# Project2023

A web-based application built with oTree, designed for conducting interactive experiments and surveys.

## Overview

This project implements a choice-based experiment/survey system that allows researchers to collect data from participants through a series of interactive pages and decision tasks.

## Features

- Interactive web interface for experiment participants
- Customizable page sequences and workflows
- Data collection and storage capabilities
- Support for various experimental designs and survey types
- Real-time participant interaction

## Technology Stack

- Python
- oTree framework
- HTML/CSS
- JavaScript
- Database backend (SQLite/PostgreSQL)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/xrshen2002/ChoiceList240206.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```
   otree devserver
   ```

## Usage

1. Access the admin interface at `http://localhost:8000/admin/`
2. Create a new session
3. Distribute the participant links to your subjects
4. Monitor progress and collect data through the admin interface

## Project Structure

- `project2023/pages.py`: Defines the page sequence and behavior
- Other oTree standard files and directories

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)

## Contact

For questions or feedback, please contact [your contact information]. 