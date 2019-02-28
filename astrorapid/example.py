from astrorapid.classify import Classify


def main(graph=None, model=None):
    """
    Example code to run astrorapid.

    Ignore the graph and model parameter inputs unless you wish to do your own multithreading.
    (Note: astrorapid already performs its own parallelisation based on a keras and tensorflow backend).
    """

    mjd = [57433.4816, 57436.4815, 57439.4817, 57451.4604, 57454.4397, 57459.3963, 57462.418, 57465.4385, 57468.3768,
           57473.3606, 57487.3364, 57490.3341, 57493.3154, 57496.3352, 57505.3144, 57513.2542, 57532.2717, 57536.2531,
           57543.2545, 57546.2703, 57551.2115, 57555.2669, 57558.2769, 57561.1899, 57573.2133, 57433.5019, 57436.4609,
           57439.4587, 57444.4357, 57459.4189, 57468.3142, 57476.355, 57479.3568, 57487.3586, 57490.3562, 57493.3352,
           57496.2949, 57505.3557, 57509.2932, 57513.2934, 57518.2735, 57521.2739, 57536.2321, 57539.2115, 57543.2301,
           57551.1701, 57555.2107, 57558.191, 57573.1923, 57576.1749, 57586.1854]
    flux = [2.0357230e+00, -2.0382695e+00, 1.0084588e+02, 5.5482742e+01, 1.4867026e+01, -6.5136810e+01, 1.6740545e+01,
            -5.7269131e+01, 1.0649184e+02, 1.5505235e+02, 3.2445984e+02, 2.8735449e+02, 2.0898877e+02, 2.8958893e+02,
            1.9793906e+02, -1.3370536e+01, -3.9001358e+01, 7.4040916e+01, -1.7343750e+00, 2.7844931e+01, 6.0861992e+01,
            4.2057487e+01, 7.1565346e+01, -2.6085690e-01, -6.8435440e+01, 17.573107, 41.445435, -110.72664, 111.328964,
            -63.48336, 352.44907, 199.59058, 429.83075, 338.5255, 409.94604, 389.71262, 195.63905, 267.13318, 123.92461,
            200.3431, 106.994514, 142.96387, 56.491238, 55.17521, 97.556946, -29.263103, 142.57687, -20.85057,
            -0.67210346, 63.353024, -40.02601]
    fluxerr = [42.784702, 43.83665, 99.98704, 45.26248, 43.040398, 44.00679, 41.856007, 49.354336, 105.86439, 114.0044,
               45.697918, 44.15781, 60.574158, 93.08788, 66.04482, 44.26264, 91.525085, 42.768955, 43.228336, 44.178196,
               62.15593, 109.270035, 174.49638, 72.6023, 48.021034, 44.86118, 48.659588, 100.97703, 148.94061, 44.98218,
               139.11194, 71.4585, 47.766987, 45.77923, 45.610615, 60.50458, 105.11658, 71.41217, 43.945534, 45.154167,
               43.84058, 52.93122, 44.722775, 44.250145, 43.95989, 68.101326, 127.122025, 124.1893, 49.952255, 54.50728,
               114.91599]
    passband = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
                'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
                'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
    zeropoint = [27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5,
                 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5,
                 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5, 27.5]
    photflag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4096, 4096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4096,
                6144, 4096, 4096, 4096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    objid = 'MSIP_01_NONIa-0001_10400862'
    ra = 3.75464531293933
    dec = 0.205076187109334
    redshift = 0.233557
    mwebv = 0.0228761

    light_curve_list = [(mjd, flux, fluxerr, passband, zeropoint, photflag, ra, dec, objid, redshift, mwebv)]

    classification = Classify(light_curve_list, known_redshift=True, graph=graph, model=model)
    predictions = classification.get_predictions()
    print(predictions)

    # classification.plot_light_curves_and_classifications(step=False)
    # classification.plot_classification_animation()
    # classification.plot_classification_animation_step()


def example_try_multi_threading():
    import threading
    import tensorflow as tf
    from keras.models import load_model

    global graph, model

    model = load_model('/Users/danmuth/PycharmProjects/astrorapid/astrorapid/keras_model_with_redshift.hdf5')

    graph = tf.get_default_graph()

    # Example running threads
    t1 = threading.Thread(target=main, args=(graph, model))
    t2 = threading.Thread(target=main, args=(graph, model))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")


if __name__ == '__main__':
    main()
