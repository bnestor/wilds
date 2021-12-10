import math

from examples.configs.datasets import dataset_defaults

AMAZON = "amazon"
CIVIL_COMMENTS = "civilcomments"
CAMELYON17 = "camelyon17"
DOMAINNET = "domainnet"
GLOBAL_WHEAT = "globalwheat"
IWILDCAM = "iwildcam"
FMOW = "fmow"
OGB = "ogb-molpcba"
POVERTY = "poverty"

# Maximum batch size that fits on a 12GB GPU
MAX_BATCH_SIZES = {
    AMAZON: 24,
    CIVIL_COMMENTS: 48,
    CAMELYON17: 168,
    DOMAINNET: 96,
    GLOBAL_WHEAT: 8,
    IWILDCAM: 24,
    FMOW: 72,
    OGB: 4096,
    POVERTY: 120,
}

DEFAULT_UNLABELED_FRAC = [3 / 4, 7 / 8, 15 / 16]

NOISY_STUDENT_TEACHERS = {
    CAMELYON17: "0xb7b57b6f117e4d48b4c6f172092ae323",
    IWILDCAM: "0x52f2dd8e448a4c7e802783fa35c269c6",
    FMOW: "0x3b7e033b88464f53a3c432614bda72d3",
    POVERTY: "0x6e908c5ef2f544a3aeab871549711084",
    OGB: "0xbef12512ae7f43b9a2f1e570be0b89df",
    GLOBAL_WHEAT: "0xc7277e7a07d0441882b242a759687935",
    DOMAINNET: "0x94ce0d6abe4345c88d524edde1137f3b",
}


def get_epochs_unlabeled(dataset, factor=1, parts=[4, 8, 16]):
    default_n_epochs = dataset_defaults[dataset]["n_epochs"]
    return [math.ceil((default_n_epochs * factor) / part) for part in parts]


def get_lr_grid(dataset, grad_accumulation=1, low_factor=10, high_factor=10):
    default_lr = dataset_defaults[dataset]["lr"]
    default_batch_size = dataset_defaults[dataset]["batch_size"]
    max_batch_size = MAX_BATCH_SIZES[dataset]
    if dataset == OGB:
        new_lr = default_lr * 10
    else:
        new_lr = default_lr * (
            (max_batch_size * grad_accumulation) / default_batch_size
        )
    # We sample a value 10^U(a, b)
    return [math.log10(new_lr / low_factor), math.log10(new_lr * high_factor)]


ERM_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        AMAZON: {
            "batch_size": [MAX_BATCH_SIZES[AMAZON]],
            "lr": get_lr_grid(AMAZON, grad_accumulation=1),
        },
        CIVIL_COMMENTS: {
            "batch_size": [MAX_BATCH_SIZES[CIVIL_COMMENTS]],
            "lr": get_lr_grid(CIVIL_COMMENTS, grad_accumulation=1),
            "groupby_fields": ["y"],
            "uniform_over_group": [True],
        },
        CAMELYON17: {
            "batch_size": [MAX_BATCH_SIZES[CAMELYON17]],
            "lr": get_lr_grid(CAMELYON17, grad_accumulation=1),
        },
        IWILDCAM: {
            "batch_size": [MAX_BATCH_SIZES[IWILDCAM]],
            "lr": get_lr_grid(IWILDCAM, grad_accumulation=1),
        },
        FMOW: {
            "batch_size": [MAX_BATCH_SIZES[FMOW]],
            "lr": get_lr_grid(FMOW, grad_accumulation=1),
        },
        POVERTY: {
            "batch_size": [MAX_BATCH_SIZES[POVERTY]],
            "lr": get_lr_grid(POVERTY, grad_accumulation=1),
        },
        GLOBAL_WHEAT: {
            "batch_size": [MAX_BATCH_SIZES[GLOBAL_WHEAT]],
            "lr": get_lr_grid(GLOBAL_WHEAT, grad_accumulation=1),
        },
        OGB: {
            "batch_size": [MAX_BATCH_SIZES[OGB]],
            "lr": get_lr_grid(OGB, grad_accumulation=1),
        },
        DOMAINNET: {
            "batch_size": [MAX_BATCH_SIZES[DOMAINNET]],
            "lr": [-4, -2],
        },
    },
}

ERM_AUGMENT_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        CAMELYON17: {
            "batch_size": [MAX_BATCH_SIZES[CAMELYON17]],
            "lr": get_lr_grid(CAMELYON17, grad_accumulation=1),
            "additional_train_transform": ["randaugment"],
        },
        IWILDCAM: {
            "batch_size": [MAX_BATCH_SIZES[IWILDCAM]],
            "lr": get_lr_grid(IWILDCAM, grad_accumulation=1),
            "additional_train_transform": ["randaugment"],
        },
        FMOW: {
            "batch_size": [MAX_BATCH_SIZES[FMOW]],
            "lr": get_lr_grid(FMOW, grad_accumulation=1),
            "additional_train_transform": ["randaugment"],
        },
        POVERTY: {
            "batch_size": [MAX_BATCH_SIZES[POVERTY]],
            "lr": get_lr_grid(POVERTY, grad_accumulation=1),
            "additional_train_transform": ["randaugment"],
        },
        DOMAINNET: {
            "batch_size": [MAX_BATCH_SIZES[DOMAINNET]],
            "lr": [-4, -2],
            "additional_train_transform": ["randaugment"],
        },
    },
}

ERM_ORACLE_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        AMAZON: {
            "use_unlabeled_y": [True],
            "batch_size": [16],
            "unlabeled_batch_size": [8],
            "n_epochs": [4],
            "lr": get_lr_grid(AMAZON, grad_accumulation=1),
        },
        CIVIL_COMMENTS: {
            "use_unlabeled_y": [True],
            "batch_size": [10],
            "unlabeled_batch_size": [38],
            "n_epochs": [3],
            "lr": get_lr_grid(CIVIL_COMMENTS, grad_accumulation=1),
            "groupby_fields": ["y"],
            "uniform_over_group": [True],
        },
        FMOW: {
            "use_unlabeled_y": [True],
            "batch_size": [32],
            "unlabeled_batch_size": [40],
            "n_epochs": [55],
            "lr": get_lr_grid(FMOW, grad_accumulation=1),
            "additional_train_transform": ["randaugment"],
        },
        IWILDCAM: {
            "use_unlabeled_y": [True],
            "batch_size": [4],
            "unlabeled_batch_size": [20],
            "n_epochs": [10],
            "lr": get_lr_grid(IWILDCAM, grad_accumulation=1),
            "additional_train_transform": ["randaugment"],
        },
    },
}

CORAL_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        AMAZON: {
            "lr": get_lr_grid(AMAZON, grad_accumulation=4),
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(AMAZON, factor=2),
        },
        CAMELYON17: {
            "lr": get_lr_grid(CAMELYON17, grad_accumulation=4),
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(CAMELYON17, factor=2),
        },
        IWILDCAM: {
            "lr": get_lr_grid(IWILDCAM, grad_accumulation=4),
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(IWILDCAM, factor=2),
        },
        FMOW: {
            "lr": get_lr_grid(FMOW, grad_accumulation=4),
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(FMOW, factor=2),
        },
        OGB: {
            "lr": get_lr_grid(OGB, grad_accumulation=4),
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(OGB, factor=2),
        },
        POVERTY: {
            "lr": get_lr_grid(POVERTY, grad_accumulation=4),
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(POVERTY, factor=2),
        },
        DOMAINNET: {
            "lr": get_lr_grid(DOMAINNET, grad_accumulation=4),
            "coral_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(DOMAINNET, factor=2),
        },
    },
}

DANN_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        AMAZON: {
            "dann_classifier_lr": get_lr_grid(AMAZON, grad_accumulation=4),
            "dann_discriminator_lr": get_lr_grid(AMAZON, grad_accumulation=4),
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(AMAZON, factor=2),
        },
        CAMELYON17: {
            "dann_classifier_lr": get_lr_grid(CAMELYON17, grad_accumulation=4),
            "dann_discriminator_lr": get_lr_grid(CAMELYON17, grad_accumulation=4),
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(CAMELYON17, factor=2),
        },
        IWILDCAM: {
            "dann_classifier_lr": get_lr_grid(IWILDCAM, grad_accumulation=4),
            "dann_discriminator_lr": get_lr_grid(IWILDCAM, grad_accumulation=4),
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(IWILDCAM, factor=2),
        },
        FMOW: {
            "dann_classifier_lr": get_lr_grid(FMOW, grad_accumulation=4),
            "dann_discriminator_lr": get_lr_grid(FMOW, grad_accumulation=4),
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(FMOW, factor=2),
        },
        OGB: {
            "dann_classifier_lr": get_lr_grid(OGB, grad_accumulation=4),
            "dann_discriminator_lr": get_lr_grid(OGB, grad_accumulation=4),
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(OGB, factor=2),
        },
        POVERTY: {
            "dann_classifier_lr": get_lr_grid(POVERTY, grad_accumulation=4),
            "dann_discriminator_lr": get_lr_grid(POVERTY, grad_accumulation=4),
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(POVERTY, factor=2),
        },
        DOMAINNET: {
            "dann_classifier_lr": get_lr_grid(DOMAINNET, grad_accumulation=4),
            "dann_discriminator_lr": get_lr_grid(DOMAINNET, grad_accumulation=4),
            "dann_penalty_weight": [-1, 1],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(DOMAINNET, factor=2),
        },
    },
}

AFN_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        AMAZON: {
            "lr": get_lr_grid(AMAZON, grad_accumulation=4, high_factor=1),
            "afn_penalty_weight": [-4, -2],
            "safn_delta_r": [1],
            "unlabeled_batch_size_frac": [0.5],
            "n_epochs": get_epochs_unlabeled(AMAZON, factor=2, parts=[2]),
        },
        CAMELYON17: {
            "lr": get_lr_grid(CAMELYON17, grad_accumulation=4, high_factor=1),
            "afn_penalty_weight": [-4, -2],
            "safn_delta_r": [1],
            "unlabeled_batch_size_frac": [0.5],
            "n_epochs": get_epochs_unlabeled(CAMELYON17, factor=2, parts=[2]),
        },
        IWILDCAM: {
            "lr": get_lr_grid(IWILDCAM, grad_accumulation=4, high_factor=1),
            "afn_penalty_weight": [-4, -2],
            "safn_delta_r": [1],
            "unlabeled_batch_size_frac": [0.5],
            "n_epochs": get_epochs_unlabeled(IWILDCAM, factor=2, parts=[2]),
        },
        FMOW: {
            "lr": get_lr_grid(FMOW, grad_accumulation=4, high_factor=1),
            "afn_penalty_weight": [-4, -2],
            "safn_delta_r": [1],
            "unlabeled_batch_size_frac": [0.5],
            "n_epochs": get_epochs_unlabeled(FMOW, factor=2, parts=[2]),
        },
        OGB: {
            "lr": get_lr_grid(OGB, grad_accumulation=4, high_factor=1),
            "afn_penalty_weight": [-4, -2],
            "safn_delta_r": [1],
            "unlabeled_batch_size_frac": [0.5],
            "n_epochs": get_epochs_unlabeled(OGB, factor=2, parts=[2]),
        },
        POVERTY: {
            "lr": get_lr_grid(POVERTY, grad_accumulation=4, high_factor=1),
            "afn_penalty_weight": [-4, -2],
            "safn_delta_r": [1],
            "unlabeled_batch_size_frac": [0.5],
            "n_epochs": get_epochs_unlabeled(POVERTY, factor=2, parts=[2]),
        },
        DOMAINNET: {
            "lr": get_lr_grid(DOMAINNET, grad_accumulation=4, high_factor=1),
            "afn_penalty_weight": [-4, -2],
            "safn_delta_r": [1],
            "unlabeled_batch_size_frac": [0.5],
            "n_epochs": get_epochs_unlabeled(DOMAINNET, factor=2, parts=[2]),
        },
    },
}

FIXMATCH_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        CAMELYON17: {
            "lr": get_lr_grid(CAMELYON17, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(CAMELYON17, factor=2),
        },
        IWILDCAM: {
            "lr": get_lr_grid(IWILDCAM, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(IWILDCAM, factor=2),
        },
        FMOW: {
            "lr": get_lr_grid(FMOW, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(FMOW, factor=2),
        },
        POVERTY: {
            "lr": get_lr_grid(POVERTY, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(POVERTY, factor=2),
        },
        DOMAINNET: {
            "lr": get_lr_grid(DOMAINNET, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(DOMAINNET, factor=2),
        },
    },
}

PSEUDOLABEL_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        AMAZON: {
            "lr": get_lr_grid(AMAZON, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(AMAZON, factor=2),
        },
        CIVIL_COMMENTS: {
            "lr": get_lr_grid(CIVIL_COMMENTS, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(CIVIL_COMMENTS, factor=2),
            "groupby_fields": ["y"],
            "uniform_over_group": [True],
        },
        CAMELYON17: {
            "lr": get_lr_grid(CAMELYON17, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(CAMELYON17, factor=2),
        },
        IWILDCAM: {
            "lr": get_lr_grid(IWILDCAM, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(IWILDCAM, factor=2),
        },
        FMOW: {
            "lr": get_lr_grid(FMOW, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(FMOW, factor=2),
        },
        OGB: {
            "lr": get_lr_grid(OGB, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(OGB, factor=2),
        },
        GLOBAL_WHEAT: {
            "lr": get_lr_grid(GLOBAL_WHEAT, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(GLOBAL_WHEAT, factor=2),
        },
        POVERTY: {
            "lr": get_lr_grid(POVERTY, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(POVERTY, factor=2),
        },
        DOMAINNET: {
            "lr": get_lr_grid(DOMAINNET, grad_accumulation=4),
            "self_training_lambda": [1],
            "self_training_threshold": [0.7, 0.95],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "scheduler": ["FixMatchLR"],
            "n_epochs": get_epochs_unlabeled(DOMAINNET, factor=2),
        },
    },
}

NOISY_STUDENT_HYPERPARAMETER_SEARCH_SPACE = {
    "datasets": {
        CAMELYON17: {
            "lr": get_lr_grid(CAMELYON17, grad_accumulation=4),
            "scheduler": ["FixMatchLR"],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(CAMELYON17),
        },
        IWILDCAM: {
            "lr": get_lr_grid(IWILDCAM, grad_accumulation=4),
            "scheduler": ["FixMatchLR"],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(IWILDCAM),
        },
        FMOW: {
            "lr": get_lr_grid(FMOW, grad_accumulation=4),
            "scheduler": ["FixMatchLR"],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(FMOW),
        },
        POVERTY: {
            "lr": get_lr_grid(POVERTY, grad_accumulation=4),
            "scheduler": ["FixMatchLR"],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(POVERTY),
        },
        OGB: {
            "lr": get_lr_grid(OGB, grad_accumulation=4),
            "scheduler": ["FixMatchLR"],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(OGB),
            "noisystudent_dropout_rate": [0],
        },
        GLOBAL_WHEAT: {
            "lr": get_lr_grid(GLOBAL_WHEAT, grad_accumulation=4),
            "scheduler": ["FixMatchLR"],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(GLOBAL_WHEAT),
            "self_training_threshold": [0.5, 0.7],
        },
        DOMAINNET: {
            "lr": get_lr_grid(DOMAINNET, grad_accumulation=4),
            "scheduler": ["FixMatchLR"],
            "unlabeled_batch_size_frac": DEFAULT_UNLABELED_FRAC,
            "n_epochs": get_epochs_unlabeled(DOMAINNET),
        },
    },
}