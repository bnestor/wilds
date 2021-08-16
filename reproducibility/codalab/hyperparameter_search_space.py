MAX_BATCH_SIZES = {
    "amazon": 32,
    "civilcomments": 64,
    "camelyon17": 224,
    "iwildcam": 32,
    "fmow": 96,
    "poverty": 160,
}

MULTI_GPU_ALGORITHMS = ["FixMatch", "PseudoLabel", "NoisyStudent"]

ERM_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        "amazon": {
            "batch_size": [MAX_BATCH_SIZES["amazon"]],
            "lr": [-6, -4],
            "weight_decay": [-3, -1],
        },
        "civilcomments": {
            "batch_size": [MAX_BATCH_SIZES["civilcomments"]],
            "lr": [-6, -4],
        },
        "camelyon17": {
            "batch_size": [32],
            "lr": [-4, -2],
            "weight_decay": [-3, -1],
        },
        "iwildcam": {
            "batch_size": [MAX_BATCH_SIZES["iwildcam"]],
            "lr": [-5, -3],
            "weight_decay": [-4, -1],
        },
        "fmow": {
            "batch_size": [96],
            "lr": [-5, -3],
            "weight_decay": [-5, -3],
        },
        "poverty": {
            "batch_size": [MAX_BATCH_SIZES["poverty"]],
            "lr": [-5, -1],
            "weight_decay": [-4, 0],
        },
    },
}

ERM_AUGMENT_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        "amazon": {
            "batch_size": [MAX_BATCH_SIZES["amazon"]],
            "lr": [-6, -4],
            "weight_decay": [-3, -1],
            "additional_train_transform": ["randaugment"],
        },
        "civilcomments": {
            "batch_size": [MAX_BATCH_SIZES["civilcomments"]],
            "lr": [-6, -4],
            "additional_train_transform": ["randaugment"],
        },
        "camelyon17": {
            "batch_size": [32],
            "lr": [-4, -2],
            "weight_decay": [-3, -1],
            "additional_train_transform": ["randaugment"],
        },
        "iwildcam": {
            "batch_size": [MAX_BATCH_SIZES["iwildcam"]],
            "lr": [-5, -3],
            "weight_decay": [-4, -1],
            "additional_train_transform": ["randaugment"],
        },
        "fmow": {
            "batch_size": [96],
            "lr": [-5, -3],
            "weight_decay": [-5, -3],
            "additional_train_transform": ["randaugment"],
        },
        "poverty": {
            "batch_size": [MAX_BATCH_SIZES["poverty"]],
            "lr": [-5, -1],
            "weight_decay": [-4, 0],
            "additional_train_transform": ["randaugment"],
        },
    },
}

CORAL_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        "amazon": {
            "lr": [-6, -4],
            "weight_decay": [-3, -1],
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "civilcomments": {
            "lr": [-6, -4],
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "camelyon17": {
            "lr": [-4, -2],
            "weight_decay": [-3, -1],
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "iwildcam": {
            "lr": [-5, -3],
            "weight_decay": [-4, -1],
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "fmow": {
            "lr": [-5, -3],
            "weight_decay": [-5, -3],
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "poverty": {
            "lr": [-5, -1],
            "weight_decay": [-4, 0],
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
    },
}

DANN_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        "amazon": {
            "weight_decay": [-3, -1],
            "dann_classifier_lr": [-6, -4],
            "dann_discriminator_lr": [-6, -4],
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "civilcomments": {
            "dann_classifier_lr": [-6, -4],
            "dann_discriminator_lr": [-6, -4],
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "camelyon17": {
            "weight_decay": [-3, -1],
            "dann_classifier_lr": [-4, -2],
            "dann_discriminator_lr": [-4, -2],
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "iwildcam": {
            "weight_decay": [-4, -1],
            "dann_classifier_lr": [-5, -3],
            "dann_discriminator_lr": [-5, -3],
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "fmow": {
            "weight_decay": [-5, -3],
            "dann_classifier_lr": [-5, -3],
            "dann_discriminator_lr": [-5, -3],
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
        "poverty": {
            "weight_decay": [-4, 0],
            "dann_classifier_lr": [-5, -1],
            "dann_discriminator_lr": [-5, -1],
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": [0.5, 0.9],
        },
    },
}

FIXMATCH_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        "amazon": {
            "weight_decay": [-3, -1],
            "lr": [-6, -4],
            "self_training_lambda": [-1, 1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": [3 / 4, 7 / 8, 15 / 16],
            "scheduler": ["FixMatchLR"],
        },
        "civilcomments": {
            "lr": [-6, -4],
            "self_training_lambda": [-1, 1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": [3 / 4, 7 / 8, 15 / 16],
            "scheduler": ["FixMatchLR"],
        },
        "camelyon17": {
            "n_epochs": [25],
            "lr": [-4, -2],
            "weight_decay": [-3, -1],
            "self_training_lambda": [-1, 1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": [3 / 4, 7 / 8, 15 / 16],
            "scheduler": ["FixMatchLR"],
        },
        "iwildcam": {
            "weight_decay": [-4, -1],
            "lr": [-5, -3],
            "self_training_lambda": [-1, 1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": [3 / 4, 7 / 8, 15 / 16],
        },
        "fmow": {
            "n_epochs": [75],
            "lr": [-5, -3],
            "weight_decay": [-5, -3],
            "self_training_lambda": [-1, 1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": [3 / 4, 7 / 8, 15 / 16],
            "scheduler": ["FixMatchLR"],
        },
        "poverty": {
            "weight_decay": [-4, 0],
            "lr": [-5, -1],
            "self_training_lambda": [-1, 1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": [3 / 4, 7 / 8, 15 / 16],
            "scheduler": ["FixMatchLR"],
        },
    },
}
