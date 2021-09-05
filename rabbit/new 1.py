def rm_bg(inName, outName):
    src = cv2.imread('/tmp/'+inName, 1)
    origina_height = src.shape[0]
    original_width = src.shape[1]
    multiplier = origina_height / original_width
    width = 1000
    height = int(1000 * multiplier)
    dim = (width, height)
    # resize image
    src = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)

    """
    reszta kodu do uswania tła
    """
    dim = (origina_height, original_width)
    foreground = cv2.resize(src, dim, interpolation = cv2.INTER_AREA) #foreground to nazwa src po usunięciu
    cv2.imwrite('/tmp/' + outName, foreground)