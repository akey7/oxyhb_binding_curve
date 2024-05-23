class OxyHbBindingCurve:
    def __init__(self, ph=7.4, temp_c=37.0):
        """
        Instantiates a new instance of a binding curve object to be calculated
        using the given parameters. Also, it defines a number of constants
        given in the table.

        Parameters
        ----------
        ph : float
            Intracellular pH. Default 7.4.

        temp_c : float
            Temperature in celsius. Default 37.0
        """

        self.k2dd = 1.0e-6  # M
        self.k3dd = 1.0e-6  # M
        self.k5dd = 2.4e-8  # M
        self.k6dd = 1.2e-8  # M
        self.k3d = 11.3  # M^-1, could also be 14.7 depending on reference
        self.w_pl = 0.94
        self.ideal_gas_const = 62.36   # (L*mmHg) / (mol*K)

        self.temp_c = temp_c
        self.ph = ph

        self.h_plus_M = 10**(-ph)

    @property
    def alpha_o2(self):
        """
        Returns
        -------
        alpha_o2 : float
            Units M/mmHg
        """
        return (1.37 - 1.37e-2*(self.temp_c-37.0) + 5.8e-4*(self.temp_c-37.0)**2) * (1.0e-6 / self.w_pl)

    @property
    def alpha_co2(self):
        """
        Returns
        -------
        alpha_co2 : float
            Units M/mmHg
        """
        return (3.07 - 5.7e-2*(self.temp_c-37.0) + 2.0e-3*(self.temp_c-37.0)**2) * (1.0e-5 / self.w_pl)

    @property
    def phi_1(self):
        """
        Returns
        -------
        phi_1 : float
            Unitless (units cancel out)
        """
        return 1 + self.k2dd / self.h_plus_M

    @property
    def phi_2(self):
        """
        Returns
        -------
        phi_2 : float
            Unitless (units cancel out)
        """
        return 1 + self.k3dd / self.h_plus_M
    
    @property
    def phi_3(self):
        """
        Returns
        -------
        phi_3 : float
            Unitless (units cancel out)
        """
        return 1 + self.h_plus_M / self.k5dd
    
    @property
    def phi_4(self):
        """
        Returns
        -------
        phi_4
            Unitless (units cancel out)
        """
        return 1 + self.h_plus_M / self.k6dd

    def __str__(self):
        return f"pco2_mmhg={self.pco2_mmhg} two_three_dpg_M={self.two_three_dpg} temp_c={self.temp_c} ph={self.ph}"


if __name__ == '__main__':
    oxy_hb_binding_curve = OxyHbBindingCurve()
    print(f'alpha_o2={oxy_hb_binding_curve.alpha_o2}, alpha_co2={oxy_hb_binding_curve.alpha_co2}')
