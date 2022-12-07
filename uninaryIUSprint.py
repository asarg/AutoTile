# Hack Research Plan

# 1. Make a table class
## 1.1 Make the east edge of the table

### A) Write a table edge door function that takes in an x and y and returns an inactive door gadget with a len 1 wire on the east side
### and a len 3 wire on west side

### B) Add door handles to the door

### C) Add signal gap tiles and corners

### D) Get door to recognize a data string has arrived and wait for confirmation before opening

### E) Get door to open when signal is received

### F) Get door to close but wait for table completion after data passed through

### G) Stack 3 doors on top of each other and confirm pass waiting up and down

# 2. Make Macrocell Class
## 2.1 Make a macrocell that can be placed on the table

## 2.2. Make Active Table Column

## 2.3. Make Table Transition

## 2.4. Make Table Reset Doors

# 3. Make Table Communicate Acceptance/Rejection of State Change

## 3.1. Make Neighboring Block Finalize State Change

## 3.2. Make Table Transmit New State to Adjacent Super Blocks

# 4. Program Construction of Table

# 5. Program Construction of Seed

# 6. Program Construction of New Super Blocks

if __name__ == "__main__":
    #system = make_system()
    #SaveFile.main(system, ["uniaryWiresIUTest.xml"])
    print("Done")
