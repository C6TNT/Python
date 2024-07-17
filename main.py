def _do_python_eval(self, output_dir='output'):
    annopath = os.path.join(

        self._devkit_path,

        'VOC' + self._year,

        'Annotations',

        '{:s}.xml')

    imagesetfile = os.path.join(

        self._devkit_path,

        'VOC' + self._year,

        'ImageSets',

        'Main',

        self._image_set + '.txt')

    cachedir = os.path.join(self._devkit_path, 'annotations_cache')

    aps = []

    # The PASCAL VOC metric changed in 2010

    use_07_metric = True if int(self._year) < 2010 else False

    print('VOC07 metric? ') + ('Yes' if use_07_metric else 'No')

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    for i, cls in enumerate(self._classes):

        if cls == '__background__':
            continue

        filename = self._get_voc_results_file_template().format(cls)

        rec, prec, ap = voc_eval(

            filename, annopath, imagesetfile, cls, cachedir, ovthresh=0,

            use_07_metric=use_07_metric)

        aps += [ap]

        pl.plot(rec, prec, lw=2,

                label='{} (AP = {:.4f})'

                      ''.format(cls, ap))

        print('AP for {} = {:.4f}'.format(cls, ap))

        with open(os.path.join(output_dir, cls + '_pr.pkl'), 'w') as f:

            cPickle.dump({'rec': rec, 'prec': prec, 'ap': ap}, f)

    pl.xlabel('Recall')

    pl.ylabel('Precision')

    plt.grid(True)

    pl.ylim([0.0, 1.05])

    pl.xlim([0.0, 1.05])

    pl.title('Precision-Recall')

    pl.legend(loc="lower left")

    plt.savefig('./PR.jpg')

    plt.show()

    print('Mean AP = {:.4f}'.format(np.mean(aps)))

    print('~~~~~~~~')

    print('Results:')

    for ap in aps:
        print('{:.3f}'.format(ap))

    print('{:.3f}'.format(np.mean(aps)))

    print('~~~~~~~~')

    print('')

    print('--------------------------------------------------------------')

    print('Results computed with the **unofficial** Python eval code.')

    print('Results should be very close to the official MATLAB eval code.')

    print('Recompute with `./tools/reval.py --matlab ...` for your paper.')

    print('-- Thanks, The Management')

    print('--------------------------------------------------------------')

————————————————
版权声明：本文为CSDN博主「qq_53951219」的原创文章，遵循CC
4.0
BY - SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / qq_53951219 / article / details / 127407874
