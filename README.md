# Insurance charge prediction

Fits training-only numeric/categorical preprocessing and a dense neural-network regressor for insurance charges.

## Setup and execution

Use Python 3.11 and a separate virtual environment for this project. Run commands from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python check_inputs.py
python -m jupyterlab
```

On Windows, activate with `.venv\Scripts\activate`. For notebooks, select this environment’s kernel and execute from the top in a fresh kernel. The first code cell exposes `INPUT_PATHS` where old machine-specific paths existed. `PROJECT_DATA_DIR` changes the base for those configured paths; remaining relative paths use the notebook working directory.

## Notebooks

- [Insurance_Payment_Prediction_using_Regression.ipynb](Insurance_Payment_Prediction_using_Regression.ipynb)

## Inputs

Supply these inputs yourself; no dataset is downloaded automatically:

- `insurance.csv`

## Outputs

An in-memory regression model and mean absolute error.

## Implementation and limitations

CSV requires age, sex, bmi, children, smoker, region, and charges. Supply the file locally; the notebook no longer retrieves a changing remote CSV during execution. Dense architecture and the 200-epoch schedule are retained.

Reusable model/analysis functions live in `experiment_insurance_payment_prediction_using_regression.py`. Notebooks retain the experiment sequence, training, and visual narrative.

## Verification

The workspace regression suite checks source/notebook validity and selected behavior with bundled or synthetic inputs. Full experiment training and historical metric reproduction are not implied. See the workspace `REFACTOR_REPORT.md` for exact test coverage and unresolved runtime requirements.
