Write-Host "Start editing video." -ForegroundColor Green

Write-Host "Crop the clip:" -ForegroundColor Green
python3 main.py --crop --outFile 'ClipRaw' --inFile 'ClipCrop' -x 37 -y 160 -wd 576 -ht 667

Write-Host "Make subclips:" -ForegroundColor Green
python3 main.py --subClip --outFile 'ClipCrop' --inFile 'SubClipRaw1' --start 3 --end 8
python3 main.py --subClip --outFile 'ClipCrop' --inFile 'SubClipRaw2' --start 9 --end 14
python3 main.py --subClip --outFile 'ClipCrop' --inFile 'SubClipRaw3' --start 15 --end 20

Write-Host "Add fade effect:" -ForegroundColor Green
python3 main.py --addFade --outFile 'SubClipRaw1' --inFile 'ClipWithFade1' --duration 1.1
python3 main.py --addFade --outFile 'SubClipRaw2' --inFile 'ClipWithFade2' --duration 1.1
python3 main.py --addFade --outFile 'SubClipRaw3' --inFile 'ClipWithFade3' --duration 1.1

Write-Host "Concatenate videoclips:" -ForegroundColor Green
python3 main.py --joinClips --name 'ClipWithFade' --count 3 --inFile 'JoinClip'

Write-Host "Deleting" -ForegroundColor Yellow
Remove-Item "video/ClipCrop.avi"  

Remove-Item "video/SubClipRaw1.avi" 
Remove-Item "video/SubClipRaw2.avi" 
Remove-Item "video/SubClipRaw3.avi" 

Remove-Item "video/ClipWithFade1.avi" 
Remove-Item "video/ClipWithFade2.avi" 
Remove-Item "video/ClipWithFade3.avi" 

Write-Host "End editing video." -ForegroundColor Green