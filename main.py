from bs4 import *
import requests
import os


def folder_create():
    try:
        folder_name = input("Enter Folder Name: ")
        os.mkdir(folder_name)
    except:
        print("Folder Exist with that name!")
        folder_create()

def run(url):
    print(url)
    folder_create()


if __name__ == "__main__":
    run("https://www.instagram.com/p/CR38k-HDTMm/")
