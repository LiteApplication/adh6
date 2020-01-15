/**
 * Adherent
 * Adherent api
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

export interface MembershipRequest { 
    /**
     * Duration in days
     */
    duration: number;
    paymentMethod?: MembershipRequest.PaymentMethodEnum;
}
export namespace MembershipRequest {
    export type PaymentMethodEnum = 'cash' | 'card' | 'bank_cheque';
    export const PaymentMethodEnum = {
        Cash: 'cash' as PaymentMethodEnum,
        Card: 'card' as PaymentMethodEnum,
        BankCheque: 'bank_cheque' as PaymentMethodEnum
    };
}