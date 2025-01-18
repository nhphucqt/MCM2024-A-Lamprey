# Configuration

The configuration file `config.py` contains the initial conditions and parameters for the simulation.

## Initial Condition
`y0`: Initial state vector representing the starting values for the simulation. The meaning of `y0`:
- `y0[0]`: C - Population density of sex-undetermined sea lamprey whose growth rate is not greatly affected by the environment,
- `y0[1]`: Fast - Population density of sex-undetermined sea lamprey experiencing favorable growth environment,
- `y0[2]`: Slow - Population density of sex-undetermined sea lamprey experiencing unfavorable growth environment,
- `y0[3]`: F - Population density of adult female sea lamprey,
- `y0[4]`: M - Population density of adult male sea lamprey,
- `y0[5]`: O - Population density of other sea creatures in the downstream environment,
- `y0[6]`: E - Population density of sea lamprey eggs,

## Parameters
- `T_HP`: Period for the high phase function.
- `T_MP`: Period for the medium phase function.
- `K_upstream`: Carrying capacity upstream.
- `K_downstream`: Carrying capacity downstream.
- `p_E_to_E`: Transition probability from eggs to eggs.
- `p_E_to_C`: Transition probability from eggs to undetermined sea lamprey.
- `p_C_to_C`: Transition probability for undetermined sea lamprey to remain in the same state.
- `p_C_to_Fast`: Transition probability from undetermined sea lamprey to favorable growth environment.
- `p_C_to_Slow`: Transition probability from undetermined sea lamprey to unfavorable growth environment.
- `p_Fast_to_Fast`: Transition probability for sea lamprey in favorable growth environment to remain in the same state.
- `p_Slow_to_Slow`: Transition probability for sea lamprey in unfavorable growth environment to remain in the same state.
- `p_Fast_to_F`: Transition probability from favorable growth environment to adult female sea lamprey.
- `p_Slow_to_M`: Transition probability from unfavorable growth environment to adult male sea lamprey.
- `p_F_to_D`: Transition probability from adult female sea lamprey to death.
- `p_M_to_D`: Transition probability from adult male sea lamprey to death.
- `r_O`: Growth rate of other sea creatures in the downstream environment.
- `alpha`: Interaction coefficient between other sea creatures and sea lamprey.
- `mu`: Reproduction rate of sea lamprey.
- `beta`: Model constant for interaction term.
- `gamma`: Model constant for phase function interaction.

## Simulation Parameters
- `dt`: Time step for the simulation.
- `T`: Total time for the simulation.
- `num_time_pts`: Number of time points, calculated as `int(T / dt)`.
- `t`: Time vector, generated using `np.linspace(0, T, num_time_pts)`.

# Usage

```bash
python demo.py
```