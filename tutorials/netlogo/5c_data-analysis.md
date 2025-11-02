# Exporting Data for External Analysis (15 min)

Sometimes you need more sophisticated analysis than NetLogo provides. Exporting data lets you use Excel, R, Python, or other tools.

## File Output Commands

**Write data to CSV files** that other programs can read:

```ruby
; Open file for writing (do this in setup)
file-open "model-output.csv"
file-print "tick,cooperators,defectors,mean-payoff"
file-close

; Write data each tick (do this in go procedure)
file-open "model-output.csv"
file-print (word ticks "," 
                 count turtles with [strategy = "cooperate"] ","
                 count turtles with [strategy = "defect"] ","
                 mean [payoff] of turtles)
file-close
```

**Better approach using procedures:**

```ruby
to setup
  ; ... other setup code ...
  setup-output-file
end

to setup-output-file
  ; Delete old file and create new one with headers
  if file-exists? "results.csv" [ file-delete "results.csv" ]
  file-open "results.csv"
  file-print "tick,cooperation_rate,mean_payoff,clustering"
  file-close
end

to record-data
  file-open "results.csv"
  let coop-rate count turtles with [strategy = "cooperate"] / count turtles
  let avg-payoff mean [payoff] of turtles
  let clustering-measure calculate-clustering  ; Your custom measure
  
  file-print (word ticks "," coop-rate "," avg-payoff "," clustering-measure)
  file-close
end

to go
  ; ... model update code ...
  record-data  ; Call this every tick or every N ticks
  tick
end
```

## Network Analysis Output

**Export network structure** for analysis in specialized tools:

```ruby
to export-network
  ; Export edge list
  file-open "network-edges.csv"
  file-print "source,target,weight"
  ask links [
    file-print (word [who] of end1 "," [who] of end2 "," link-weight)
  ]
  file-close
  
  ; Export node attributes
  file-open "network-nodes.csv"
  file-print "id,strategy,payoff,degree"
  ask turtles [
    file-print (word who "," strategy "," payoff "," count link-neighbors)
  ]
  file-close
end
```

## Spatial Data Output

**Export spatial patterns** for GIS or mapping analysis:

```ruby
to export-spatial-data
  file-open "spatial-data.csv"
  file-print "x,y,population,wealth,satisfaction"
  ask patches [
    if count turtles-here > 0 [
      file-print (word pxcor "," pycor "," 
                       count turtles-here ","
                       mean [wealth] of turtles-here ","
                       mean [satisfaction] of turtles-here)
    ]
  ]
  file-close
end
```

## Activity: Data Export Practice

**Choose one type of data export and implement it:**

1. **Time series:** Track 3-4 key variables over time
2. **Network data:** Export agent connections and attributes  
3. **Spatial data:** Export location-based information
4. **Test your export** by running model and checking output file

```{admonition} Data Export Best Practices
:class: tip

**Use standard formats:**
- CSV for most data (Excel, R, Python can all read it)
- JSON for complex nested data
- GML or GraphML for networks

**Include metadata:**
- Parameter values used
- Date and time of run
- Model version
- Random seed (for reproducibility)

**Organize output files:**
- Create separate folder for data
- Use meaningful filenames (model-name_date_parameters.csv)
- Include documentation explaining what each column means

**Test with small runs first:**
- Make sure data looks reasonable
- Check that files open correctly in other programs
- Verify calculations are correct
```

## Reproducible Research

**Document your analysis process:**

1. **Save parameter settings** used for each analysis
2. **Record random seeds** so others can reproduce exact results
3. **Document data processing steps** from model output to final conclusions
4. **Share both model files and analysis scripts**
