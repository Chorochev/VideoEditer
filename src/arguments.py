import argparse

def init():
    global args

    example_text = '''examples:
    python3 %(prog)s --help
    python3 %(prog)s --record --inFile 'ClipRaw'
    python3 %(prog)s --crop --outFile 'ClipRaw' --inFile 'ClipCrop' -x 37 -y 160 -wd 576 -ht 665
    python3 %(prog)s --slowDown --outFile 'ClipCrop' --inFile 'ClipSlow' --speedRatio 0.66
    python3 %(prog)s --addTitle --outFile 'ClipCrop' --inFile 'ClipWithTitle' --caption 'SELECT'
    python3 %(prog)s --addFade --outFile 'ClipCrop' --inFile 'ClipWithFade' --duration 2.1 
    python3 %(prog)s --subClip --outFile 'ClipRaw' --inFile 'SubClip' --start 10 --end 13
    '''

    parser = argparse.ArgumentParser(description='Helper for creating video clips.',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    # Record
    parser.add_argument('--record', action='store_true', 
                        help='Screen video recording. Press CTRL+C to stop recording.')
    
    parser.add_argument('--inFile', type=str, help='Save to file.')
    parser.add_argument('--outFile', type=str, help='Read file.')
    
    # Crop
    parser.add_argument('--crop', action='store_true', help='Crop video.')
    parser.add_argument('-x', type=int, help='X-axis position (px).')
    parser.add_argument('-y', type=int, help='Y-axis position (px).')
    parser.add_argument('-wd', type=int, help='Width (px).')
    parser.add_argument('-ht', type=int, help='Height (px).')

    # SlowDown
    parser.add_argument('--slowDown', action='store_true', help='Make a video clip slower.')
    parser.add_argument('--speedRatio', type=float, help='Speed ​​coefficient.')

    # Title
    parser.add_argument('--addTitle', action='store_true', help='Adding titles to a video clip.')
    parser.add_argument('--caption', type=str, help='Caption.')

    # Fade
    parser.add_argument('--addFade', action='store_true', help='Adding a Fade Effect to a Video Clip.')
    parser.add_argument('--duration', type=float, help='Duration of effect.')

    # SubClip
    parser.add_argument('--subClip', action='store_true', help='Make a subclip.')
    parser.add_argument('--start', type=float, help='Start time in sec.')
    parser.add_argument('--end', type=float, help='End time in sec.')

    args = parser.parse_args()    
