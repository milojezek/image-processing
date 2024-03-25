# Print a welcome message
echo "=== Welcome to the Scan Script ==="
echo Please enter an annotation:
options=("benign_microcalsifications" "malign_microcalcifications" "malign_mass" "benign_mass")

# Display menu and get user input
select opt in "${options[@]}"
do
    case $opt in
        "benign_microcalsifications"|"malign_microcalcifications"|"malign_mass"|"benign_mass")
            echo "You chose $opt"
            input=$opt
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

# Run the Python script with a chosen annotation
python3 src/main.py "$input"