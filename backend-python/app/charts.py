import matplotlib
matplotlib.use('Agg')   # non-GUI backend (safe for FastAPI)
import matplotlib.pyplot as plt
import os

def generate_progress_chart(df):
    os.makedirs("outputs", exist_ok=True)
    output_path = os.path.join("outputs", "progress_chart.png")

    plt.figure(figsize=(6, 4))
    plt.bar(df['id'], df['progress_percent'], color='skyblue')
    plt.xlabel("Task ID")
    plt.ylabel("Progress (%)")
    plt.title("Work Progress by Task")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()
    return output_path   


def generate_materials_chart(materials_df):
    os.makedirs("outputs", exist_ok=True)
    output_path = os.path.join("outputs", "materials_chart.png")

    plt.figure(figsize=(5, 5))
    plt.pie(
        materials_df['quantity'],
        labels=materials_df['id'],
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.Paired.colors
    )
    plt.title("Material Usage Distribution")
    plt.tight_layout()

    plt.savefig(output_path) 
    plt.close()
    return output_path
