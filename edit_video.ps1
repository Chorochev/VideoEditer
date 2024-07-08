Write-Host "Start editing video." -ForegroundColor Green

Write-Host "Crop the clip:" -ForegroundColor Green
python3 main.py --crop --outFile 'ClipRaw' --inFile 'ClipCrop' -x 37 -y 160 -wd 576 -ht 667

Write-Host "Add fade effect:" -ForegroundColor Green
python3 main.py --addFade --outFile 'ClipCrop' --inFile 'ClipWithFade' --duration 2.1

Write-Host "Deleting 'video/ClipCrop.avi'" -ForegroundColor Yellow
Remove-Item "video/ClipCrop.avi"  

Write-Host "End editing video." -ForegroundColor Green