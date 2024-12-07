import pandas as pd
import sys

def analyze_checklist(file_path):
    try:
        print(f"Loading checklist from: {file_path}")
        checklist = pd.read_excel(file_path)

        # 진행 상태 분석
        total_items = len(checklist)
        completed = checklist[checklist["Status"] == "Completed"].shape[0]
        pending = total_items - completed

        print("\nChecklist Analysis:")
        print(f"Total Items: {total_items}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")

        # 결과 저장
        results_path = "results/checklist_analysis.json"
        checklist_summary = {
            "total_items": total_items,
            "completed": completed,
            "pending": pending
        }
        pd.DataFrame([checklist_summary]).to_json(results_path, orient="records")
        print(f"\nAnalysis saved to: {results_path}")

    except Exception as e:
        print(f"Error analyzing checklist: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python checklist_analyzer.py --input <file_path>")
    else:
        file_path = sys.argv[1].split("--input ")[-1]
        analyze_checklist(file_path)
