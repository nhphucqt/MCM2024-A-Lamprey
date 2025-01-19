import numpy as np

def lamprey(t, y, args):
    """
        This function defines the dynamical equations
        that represent the environmental system of the lamprey.

        Variables are as follows:
        t: time,
        y[0]: C - Population density of sex-undetermined sea lamprey whose growth rate is not greatly affected by the environment,
        y[1]: Fast - Population density of sex-undetermined sea lamprey experiencing favorable growth environment,
        y[2]: Slow - Population density of sex-undetermined sea lamprey experiencing unfavorable growth environment,
        y[3]: F - Population density of adult female sea lamprey,
        y[4]: M - Population density of adult male sea lamprey,
        y[5]: O - Population density of other sea creatures in the downstream environment,
        y[6]: E - Population density of sea lamprey eggs,

        params : dict
        Dictionary of parameters including:
        - T_HP, T_MP: Periods for the phase function.
        - K_upstream, K_downstream: Carrying capacities.
        - p_E_to_C, p_C_to_C, p_C_to_Fast, etc.: Transition probabilities.
        - beta, gamma, alpha, mu, r_O: Model constants.

        Equations:
        1. Phase Function:
            phase(t) = 
                0, if ∃ k ∈ ℤ₀⁺ such that k(T_HP + T_MP) ≤ t < k(T_HP + T_MP) + T_HP
                1, otherwise

        2. Auxiliary Variables:
            AL = F + M

        3. Dynamics:
            dC/dt = (1 - C / K_upstream) * (p_E_to_C * E - (1 - p_C_to_C) * C)
            dFast/dt = p_C_to_Fast * C - (1 - p_Fast_to_Fast) * Fast
            dSlow/dt = p_C_to_Slow * C - (1 - p_Slow_to_Slow) * Slow
            dF/dt = (1 - (F + M + O) / K_downstream) * (
                        p_Fast_to_F * Fast 
                        - (p_F_to_D * AL) / (beta * O + AL) * F 
                        - gamma * min(M, F) * phase(t)
                    )
            dM/dt = (1 - (F + M + O) / K_downstream) * (
                        p_Slow_to_M * Slow 
                        - (p_M_to_D * AL) / (beta * O + AL) * M 
                        - gamma * min(M, F) * phase(t)
                    )
            dO/dt = (1 - (F + M + O) / K_downstream) * (
                        r_O * O 
                        - alpha * O * AL
                    )
            dE/dt = -(1 - p_E_to_E) * E + mu * gamma * min(M, F) * phase(t)
    """

    # Unpack the parameters
    params = args

    # Phase function
    phase = 0 if (t % (params['T_HP'] + params['T_MP'])) < params['T_HP'] else 1

    # Auxiliary variables
    AL = y[3] + y[4]

    # Dynamics
    dC = (1 - (y[0] + y[1] + y[2]) / params['K_upstream']) * (params['p_E_to_C'] * y[6] - (1 - params['p_C_to_C']) * y[0])
    dFast = (1 - (y[0] + y[1] + y[2]) / params['K_upstream']) * (params['p_C_to_Fast'] * y[0] - (1 - params['p_Fast_to_Fast']) * y[1])
    dSlow = (1 - (y[0] + y[1] + y[2]) / params['K_upstream']) * (params['p_C_to_Slow'] * y[0] - (1 - params['p_Slow_to_Slow']) * y[2])
    dF = (1 - (AL + y[5]) / params['K_downstream']) * (
        params['p_Fast_to_F'] * y[1] - (params['p_F_to_D'] * AL) / (params['beta'] * y[5] + AL) * y[3] - params['gamma'] * min(y[4], y[3]) * phase
    )
    dM = (1 - (AL + y[5]) / params['K_downstream']) * (
        params['p_Slow_to_M'] * y[2] - (params['p_M_to_D'] * AL) / (params['beta'] * y[5] + AL) * y[4] - params['gamma'] * min(y[4], y[3]) * phase
    )
    dO = (1 - (AL + y[5]) / params['K_downstream']) * (
        params['r_O'] * y[5] - params['alpha'] * y[5] * AL
    )
    dE = -(1 - params['p_E_to_E']) * y[6] + params['mu'] * params['gamma'] * min(y[4], y[3]) * phase

    return np.array([dC, dFast, dSlow, dF, dM, dO, dE])