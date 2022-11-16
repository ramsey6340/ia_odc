from e_learning import Elearning


def main():
    elearning = Elearning('../scorm_tracking_copy.csv')
    elearning.display_n_fig_in_10_top_module()

if __name__ == "__main__":
    main()
