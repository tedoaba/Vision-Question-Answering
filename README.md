This project implements a Visual Question Answering (VQA) system using a pre-trained model from Hugging Face or a locally stored model.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Using the Default Hugging Face Model (Online Mode)](#using-the-default-hugging-face-model-online-mode)
  - [Using a Local Model (Offline Mode)](#using-a-local-model-offline-mode)
  - [Using an Image from a URL](#using-an-image-from-a-url)
  - [Running the Streamlit App](#running-the-streamlit-app)
- [Running Tests Locally](#running-tests-locally)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/tedoaba/Vision-Question-Answering.git
    cd Vision-Question-Answering
    ```
2. Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/Scripts/activate  # On Windows

    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Using the Default Hugging Face Model (Online Mode)

Run the VQA system with an image and a question:
```sh
python scripts/run_vqa.py --image "path_to_image.jpg" --question "What is the person doing?"
```

### Using a Local Model (Offline Mode)

Run the VQA system with a local model:
```sh
python scripts/run_vqa.py --image "path_to_image.jpg" --question "What is the color of the car?" --model_path "models/vqa/"
```

### Using an Image from a URL

Run the VQA system with an image URL:
```sh
python scripts/run_vqa.py --image "https://example.com/image.jpg" --question "What is happening in the image?" --url
```

### Running the Streamlit App

To run the Streamlit app, use the following command:
```sh
streamlit run app.py
```

## Running Tests Locally

To run the tests locally, follow these steps:

1. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the tests:
    ```sh
    python -m unittest discover -s tests
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
