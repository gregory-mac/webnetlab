<a name="readme-top"></a>

<!-- PROJECT NAME -->
WebNetLab
===========
An app to deploy network lab scenarios with containerized network operating systems via web-interface.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [Docker](https://docs.docker.com/engine/install/)
* [Containerlab](https://containerlab.dev/install/)
* Python 3.9
* Poetry

In addition, one must acquire desired NOS image. Example scenarios in this repository use Arista cEOS, which can be downloaded on their site after registration.

### How to run

1. Install poetry
   ```sh
   apt install python3-poetry
   ```
2. Clone the repository
   ```sh
   git clone https://github.com/gregory-mac/webnetlab.git
   ```
3. Make projects virtual environment
   ```sh
   cd webnetlab/
   poetry install
   ```
4. Make .env file inside webnetlab directory and fill it with required information
   ```sh
   cd webnetlab/
   cp .env.example .env
   nano .env
   ```
5. Create user database
   ```sh
   poetry run alembic upgrade head
   ```
6. Start the web-server
   ```sh
   poetry run python3 app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Containerlab](https://containerlab.dev/)
* [Inet-henge](https://github.com/codeout/inet-henge)
* [FastAPI](https://fastapi.tiangolo.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
