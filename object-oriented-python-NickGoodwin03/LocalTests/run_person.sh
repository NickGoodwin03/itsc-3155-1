TC_CORRECT=0 # Test Case Correct Count
TC_INCORRECT=0 # Test Case Incorrect Count

bash LocalTests/person_test.sh

# compare the output file with the expected output file
diff LocalTests/outputs/person_test_output.txt LocalTests/outputs/person_test_output_expected.txt
if [ $? -eq 0 ]; then
    #echo "Test Case 1: Correct"
    TC_CORRECT=$((TC_CORRECT+1))
else
    #echo "Test Case 1: Incorrect"
    TC_INCORRECT=$((TC_INCORRECT+1))
fi

# if TC_INCORRECT is 0, then all test cases were correct
if [ $TC_INCORRECT -eq 0 ]; then
    echo "All Test Cases Correct"
else
    echo "Person class did not pass all test cases"
fi
