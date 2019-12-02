SUBROUTINE calctheta(x,y,res)
    integer, intent(in) :: x,y 
    double precision, intent(out) :: res
    IF (x .EQ. 0) THEN
        res = (4.D0*DATAN(1.D0))/2
    ELSE
        res = atan(DBLE(y)/DBLE(x))
    ENDIF    
END SUBROUTINE


SUBROUTINE turningband2D(L,fbmN,fbm,Li,thetai,N,Bh)
    integer :: L, fbmN
    double precision :: fbm(0:L-1,0:fbmN-1)
    integer :: Li
    double precision thetai(0:Li-1)
    integer :: N
    double precision Bh(0:N-1,0:N-1)
    integer :: j,i,x,y
    double precision theta
    
    !f2py intent(in) L
    !f2py intent(in) fbmN
    !f2py intent(in) fbm
    !f2py intent(in) Li
    !f2py intent(in) thetai
    !f2py intent(in) N
    
    !f2py intent(out) Bh
    Bh(:,:)=0.0_8
    DO x=0,N-1
        DO y=0,N-1
            call calctheta(x,y,theta)
                
            DO i=0,Li-1
                j = nint( SQRT(DBLE(x)**2 + DBLE(y)**2) * abs(cos(thetai(i)-theta)))
                Bh(x,y) = Bh(x,y) + fbm(i,j)
            ENDDO
            Bh(x,y) = Bh(x,y)/SQRT(DBLE(L))
        ENDDO
    ENDDO
END SUBROUTINE


