"""Reusable experiment functions extracted from Insurance_Payment_Prediction_using_Regression.ipynb."""

from __future__ import annotations


def build_insurance_model_3_cell_9():
    """Build the original architecture without training or accessing data."""
    import tensorflow as tf

    return tf.keras.Sequential(
        [
            tf.keras.layers.Dense(100),
            tf.keras.layers.Dense(10),
            tf.keras.layers.Dense(1),
        ]
    )
