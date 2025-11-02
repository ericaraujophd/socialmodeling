# 5. Batch Run

In the previous sections, we have built a segregation model in NetLogo. We have defined the setup, created the households, and implemented the dynamics of the model.

Now it is time to run the model in batch mode to collect data for analysis. Running the model in batch mode allows us to execute multiple simulations with different parameters and collect the results without manual intervention.

Netlogo provides a built-in feature for batch runs, which can be accessed through the "Tools" menu in the NetLogo interface. Here are the steps to set up and run a batch experiment:

1. **Open the Batch Run Tool**: In the NetLogo interface, go to `Tools` > `BehaviorSpace`. This will open the BehaviorSpace window where you can define your experiments.
2. **Create a New Experiment**: Click on the `New` button to create a new experiment. You will be prompted to enter a name for your experiment and select the model you want to run.
3. **Define the Parameters**: In the experiment setup, you can define the parameters you want to vary. For our segregation model, we might want to vary the `similar-wanted` and `density` sliders. You can set the range of values for each parameter and the number of steps to take.
4. **Set the Metrics to Record**: You can specify which global variables you want to record during the simulation. For our model, we might want to record `happy-households`, `unhappy-households`, and `proportion-similarity`.
5. **Configure the Run Settings**: You can set the number of runs for each combination of parameters, the maximum number of ticks for each run, and whether to stop the run when all households are happy.
6. **Run the Experiment**: Once you have configured all the settings, click on the `Run` button to start the batch run. NetLogo will execute the simulations and collect the data based on your specifications.
7. **Analyze the Results**: After the batch run is complete, you can export the results to a CSV file for further analysis. You can use tools like Excel, R, or Python to analyze the data and visualize the results.

## Defining the paramenters

Here is an example of how to set up the parameters for the batch run:

```plaintext
Experiment Name: Segregation Batch Run 10x
Parameters:
  - similar-wanted: 10 to 90 in steps of 10
  - density: 10 to 90 in steps of 10
Metrics to Record:
  - happy-households
  - unhappy-households
  - proportion-similarity
Run Settings:
  - Number of Runs: 10
  - Max Ticks: 1000
  - Stop when all households are happy: Yes
```

:::{image} imgs/interface-v7.png
:::

## Running the Experiment

Once you have set up the experiment as described above, click on the `Run` button to start the batch run. You then have to decide where the results will be saved. Choose a location on your computer where you can easily find the CSV files later. There are four options for saving the results:

- Spreadsheet output (CSV)
- Table output
- Stats output
- Lists output

To understand the differences between these options, you can refer to the [NetLogo BehaviorSpace documentation](https://docs.netlogo.org/behaviorspace.html#table-output).

:::{image} imgs/interface-v8.png
:::

Uncheck Update View and Update Plots and Monitors to speed up the batch run.
