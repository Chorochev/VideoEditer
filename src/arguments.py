import argparse
import os

def init():
    global args

    example_text = '''examples:
    python %(prog)s --help
    python %(prog)s --record --inFile 'ClipRaw'
    python %(prog)s --crop --outFile 'ClipRaw' --inFile 'ClipResult' -x 37 -y 160 -wd 576 -ht 665
    python %(prog)s --slowDown --outFile 'ClipResult' --inFile 'ClipSlowResult' --speedRatio 0.66   
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

    args = parser.parse_args()    
