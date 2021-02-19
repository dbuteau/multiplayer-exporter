function global:ExportMultiplayer()
{
	#https://playnite.link/forum/thread-414-post-2005.html#pid2005
    $path = $PlayniteApi.Dialogs.SaveFile("Formated TXT|*.txt")
    if ($path)
    {        
        $PlayniteApi.Database.Games | Where-Object {$_.Features.name -contains "Multi-Player"} | select Name | Sort-Object | Out-File $path -Encoding utf8
        
        $PlayniteApi.Dialogs.ShowMessage("Multi-Player games exported successfully.");
    }
}

function global:GetMainMenuItems()
{
    param(
        $menuArgs
    )

    $menuItem = New-Object Playnite.SDK.Plugins.ScriptMainMenuItem
    $menuItem.Description = "Export Multiplayer"
    $menuItem.FunctionName = "ExportMultiplayer"
    $menuItem.MenuSection = "@"
    return $menuItem
}