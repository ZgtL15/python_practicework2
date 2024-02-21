{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyOyGfjVl/6qnx8vnzBtT6Aq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ZgtL15/python_practicework/blob/main/day3/ex5_GPUtest.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NOV5r6USsPD9",
        "outputId": "67bd4001-cd9d-43c6-92a3-09a14685b314"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Wed Feb 21 22:05:04 2024       \n",
            "+---------------------------------------------------------------------------------------+\n",
            "| NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |\n",
            "|-----------------------------------------+----------------------+----------------------+\n",
            "| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |\n",
            "| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |\n",
            "|                                         |                      |               MIG M. |\n",
            "|=========================================+======================+======================|\n",
            "|   0  Tesla T4                       Off | 00000000:00:04.0 Off |                    0 |\n",
            "| N/A   60C    P8              12W /  70W |      0MiB / 15360MiB |      0%      Default |\n",
            "|                                         |                      |                  N/A |\n",
            "+-----------------------------------------+----------------------+----------------------+\n",
            "                                                                                         \n",
            "+---------------------------------------------------------------------------------------+\n",
            "| Processes:                                                                            |\n",
            "|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |\n",
            "|        ID   ID                                                             Usage      |\n",
            "|=======================================================================================|\n",
            "|  No running processes found                                                           |\n",
            "+---------------------------------------------------------------------------------------+\n"
          ]
        }
      ],
      "source": [
        "!nvidia-smi\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import cupy"
      ],
      "metadata": {
        "id": "fsNOG6CUtHe3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "67KFmYLWtHZK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def cupy_calculation(N):\n",
        "  x = cupy.random.random(size =(N,N))\n",
        "  x_fft = cupy.fft.fft2(x)\n",
        "  return(x)\n",
        "\n",
        "def np_calculation(N):\n",
        "  y = np.random.random(size=(N,N))\n",
        "  y_fft = np.fft.fft2(y)\n",
        "  return(y)"
      ],
      "metadata": {
        "id": "IloHuBF6tHPj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%timeit cupy_calculation(128)\n",
        "%timeit np_calculation(128)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7YKlWMpStTs5",
        "outputId": "77eddcd0-6d80-4271-9f1e-f6bb446fdb40"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "140 µs ± 75.6 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)\n",
            "384 µs ± 24.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%timeit cupy_calculation(256)\n",
        "%timeit np_calculation(256)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-lxC8DpptUH3",
        "outputId": "0fab1b2e-0b71-420e-899d-52b05b98aada"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "109 µs ± 13.1 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)\n",
            "1.77 ms ± 320 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%timeit cupy_calculation(512)\n",
        "%timeit np_calculation(512)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "841H5ryUtbI8",
        "outputId": "15ab2d3e-6d12-48c5-baa7-dbe7c082d3b3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "191 µs ± 76.7 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)\n",
            "9.41 ms ± 244 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%timeit cupy_calculation(1024)\n",
        "%timeit np_calculation(1024)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WMpGb2Jutc7h",
        "outputId": "3c4e4aa5-db1e-46d1-b148-5fa850d5d4d3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.22 ms ± 4.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)\n",
            "39.4 ms ± 1.37 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def np_calculation_float(N):\n",
        "  y = np.random.random(size=(N,N)).astype('float32')\n",
        "  y_fft = np.fft.fft2(y)\n",
        "  return(y)"
      ],
      "metadata": {
        "id": "yiERj9H6tgiq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "np_calculation_float(128)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gMqgg8ootsnw",
        "outputId": "736c4c59-af9a-4335-cb2c-de4fea824985"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.48327237, 0.37018836, 0.9708519 , ..., 0.28901955, 0.62324923,\n",
              "        0.54521877],\n",
              "       [0.6942374 , 0.8569944 , 0.05371829, ..., 0.35639113, 0.8761398 ,\n",
              "        0.78971434],\n",
              "       [0.45810705, 0.18586364, 0.23007259, ..., 0.8338335 , 0.10042433,\n",
              "        0.46315837],\n",
              "       ...,\n",
              "       [0.9732167 , 0.45344454, 0.63181245, ..., 0.6797708 , 0.18419333,\n",
              "        0.28373498],\n",
              "       [0.11940677, 0.5068195 , 0.16376203, ..., 0.51509625, 0.89042044,\n",
              "        0.5010618 ],\n",
              "       [0.9022621 , 0.41873953, 0.5574517 , ..., 0.8185661 , 0.29359564,\n",
              "        0.6735857 ]], dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%timeit cupy_calculation(128)\n",
        "%timeit np_calculation_float(128)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hPMEfkzXtwFr",
        "outputId": "38cadae8-bd9c-4ba0-9276-8e38f66648b8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "116 µs ± 14.9 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)\n",
            "381 µs ± 12.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)\n"
          ]
        }
      ]
    }
  ]
}