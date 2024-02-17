hparams = {
            'batch_size': 256,
            'maketrain_particles': 1.4e7,
            'L1_hsize': 128,
            'L2_hsize': 64,
            'n_outputs': 1,
            'lr': 0.0015,
            }

trainparams = {
            'n_epochs': 20,
            "patience": 5,
            "best_loss": 0.17,
            'weightedlossval': 3,
            "train_sample": "distill_wjets_emd_prl", #sample for training distill_wjets_swd
            "test_sample": "distill_ttbar_emd_prl",  #sample for testing distill_ttbar_swd
            }


dirs = {
        'filedir': '/work/tbrandes/work/data/',
        'savedir': '/work/tbrandes/delme/'
    
}

bool_val = {
            "Is_displayplots": False,
            "Is_savefig": True,
            "Is_remove_padding": True,
            "Is_min_max_scaler": False,
            "Is_standard_scaler": True,
            "Is_dtrans": False,
            "Is_do_taylor": True,
            "Is_weighted_error": True,
            }
