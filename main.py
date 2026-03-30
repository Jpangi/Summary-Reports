from weekly.config    import DB_CONFIG as WEEKLY_DB_CONFIG, CSV_FILE as WEEKLY_CSV
from weekly.extract   import extract   as weekly_extract
from weekly.transform import transform as weekly_transform
from weekly.load      import load      as weekly_load

from cobra.config    import DB_CONFIG as COBRA_DB_CONFIG, CSV_FILE as COBRA_CSV
from cobra.extract   import extract   as cobra_extract
from cobra.transform import transform as cobra_transform
from cobra.load      import load      as cobra_load

if __name__ == "__main__":

    # --- Weekly Pipeline ---
    print("🔄 Running Weekly Pipeline...")
    weekly_raw   = weekly_extract(WEEKLY_CSV)
    weekly_clean = weekly_transform(weekly_raw)
    weekly_load(weekly_clean, WEEKLY_DB_CONFIG)
    print("✅ Weekly Pipeline complete!\n")

    # --- Cobra Pipeline ---
    print("🔄 Running Cobra Pipeline...")
    cobra_raw   = cobra_extract(COBRA_CSV)
    cobra_clean = cobra_transform(cobra_raw)
    cobra_load(cobra_clean, COBRA_DB_CONFIG)
    print("✅ Cobra Pipeline complete!\n")

    print("🎉 All pipelines complete!")