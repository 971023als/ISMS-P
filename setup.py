import os
import shutil

def initialize_project():
    print("Initializing ISMS-P tools...")

    # 디렉토리 생성
    directories = ["docs", "templates", "results", "scripts"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

    # 기본 템플릿 복사
    if not os.path.exists("templates/checklist.xlsx"):
        shutil.copyfile("default_templates/checklist.xlsx", "templates/checklist.xlsx")
        print("Copied default checklist to templates directory.")

    print("Setup complete! You are ready to use the ISMS-P tools.")

if __name__ == "__main__":
    initialize_project()
